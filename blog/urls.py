from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path(
        'vote-comment/<int:comment_id>/',
        views.vote_comment,
        name='vote_comment'
    ),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('base/', views.base_view, name='base'),
    path('subjects/', views.subject_list_view, name='subject_list'),

    # Create Post URL
    path('create/', views.create_post, name='create_post'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
