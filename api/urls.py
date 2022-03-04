from django.urls import path
from .views import create_short_link

urlpatterns = [
    path('', create_short_link),
]
