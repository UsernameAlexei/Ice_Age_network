from .views import SearchView
from django.urls import path


app_name = "search"

urlpatterns = [
    path('results/', SearchView.as_view(), name='search'),
]
