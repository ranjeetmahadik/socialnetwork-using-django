from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    user    = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("tweet:detail",kwargs={'pk':self.pk})
    def __str__(self):
        return str(self.content)
