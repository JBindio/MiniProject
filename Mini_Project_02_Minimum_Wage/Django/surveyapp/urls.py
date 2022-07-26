from django.urls import path
from . import views as sur

urlpatterns = [
    path('main/', sur.main),
    path('part1_01/', sur.part1_01),
    path('part1_02/', sur.part1_02),
    path('part1_03/', sur.part1_03),
]
