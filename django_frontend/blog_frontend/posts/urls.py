from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_post, name='create_post'),
    path('success/', views.success, name='success'),
]
