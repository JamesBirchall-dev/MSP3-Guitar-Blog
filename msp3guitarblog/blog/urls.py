from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('base/', views.base_view, name='base'),
    path('create/', views.create_post_view, name='create_post'),
    path('subjects/', views.subject_list_view, name='subject_list'),
]
