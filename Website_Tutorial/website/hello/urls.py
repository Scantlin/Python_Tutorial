from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hello-home'),
    path('about/', views.index, name='hello-about'),
]