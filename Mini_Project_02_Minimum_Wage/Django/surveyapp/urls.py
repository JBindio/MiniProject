from django.urls import path
from . import views as sur

urlpatterns = [
    path('test/', sur.test),
]
