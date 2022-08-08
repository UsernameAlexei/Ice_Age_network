from django.urls import path
from .views import dashboard, profile, edit_post, ProfileList, DeletePost

app_name = "ice_age"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path('edit_post/<pk>/', edit_post, name='edit_post'),
    path('delete_post/<pk>', DeletePost.as_view(), name='delete_post'),
    path("profile_list/", ProfileList.as_view(), name="profile_list"),
    path("profile/<int:pk>", profile, name="profile"),

]
