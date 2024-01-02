from django.urls import path
from .views import *

urlpatterns = [
   path('create-card/', create_card, name='create_card'),
]
