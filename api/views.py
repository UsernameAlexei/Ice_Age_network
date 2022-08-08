from rest_framework import generics
from .serializers import PostsSerializer
from ice_age.models import Posts


class PostsApiView(generics.ListAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
