from django.urls import reverse_lazy
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class UserProfileManager(models.Manager):
    use_for_related_fields = True
    def all(self):
        try:
            qs =self.get_queryset().all().exclude(user=self.instance)
        except:
            pass
        return qs
    def to_follow(self,user,to_whom):
        user_profile,created = UserProfile.objects.get_or_create(user=user)
        if to_whom in user_profile.following.all():
            user_profile.following.remove(to_whom)
            followed = False
        else:
            user_profile.following.add(to_whom)
            followed = True
        return followed
    def is_following(self,user,followed_by_user):
        user_profile,created = UserProfile.objects.get_or_create(user=user)
        if created:
            return False
        if followed_by_user in user_profile.following.all():
            return True
        return False


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    following = models.ManyToManyField(User,related_name="followed_by")

    objects = UserProfileManager()
    def __str__(self):
        return str(self.user)

    def get_following(self):
        return self.following.all().exclude(username=self.user.username)
    def get_followurl(self):
        return reverse_lazy("profiles:follow",kwargs ={"username":self.user.username})
    def get_absolute_url(self):
        return reverse_lazy("profiles:detail",kwargs ={"username":self.user.username})



def post_save_user_receiver(sender,instance,created,*args,**kwargs):
    print(instance)
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)
        
post_save.connect(post_save_user_receiver,sender=User)
