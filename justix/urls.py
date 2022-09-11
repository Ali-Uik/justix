from django.urls import path
from .views import *


urlpatterns = [
    path('', current_datetime, name='current_datetime'),
    ]

