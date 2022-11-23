from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/<slug>/', views.detail, name='detail'),
    path('<slug>/like', views.like, name='like'),

]
