from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import TweetModelSerializer
from tweets.models import Tweet
from rest_framework import permissions
from django.db.models import Q
from .pagination import StandardResultsSetPagination

class TweetListAPIView(ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self,*args,**kwargs):
        user_following_users = self.request.user.profile.get_following()
        me = self.request.user
        qs2 = Tweet.objects.filter(user=me)
        qs1 = Tweet.objects.filter(user__in=user_following_users).order_by("-timestamp")
        qs3 = Tweet.objects.all()
        q = self.request.GET.get('search',None)
        qs = qs1 | qs2
        if q is not None:
            qs = qs3.filter(Q(content__icontains=q) |
            Q(user__username__icontains=q))
        return qs


class TweetCreateAPIView(CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
