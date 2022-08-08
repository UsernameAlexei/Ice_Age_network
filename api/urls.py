from .views import PostsApiView
from django.urls import path


app_name = "api"

urlpatterns = [
    path("posts/", PostsApiView.as_view(), name="posts_api"),
]
