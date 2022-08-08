from .views import reg_user
from django.urls import path


app_name = "reg"

urlpatterns = [
    path("", reg_user, name="registration"),
]
