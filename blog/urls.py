from django.urls import path, include
from . import views
from .views import vote_post

urlpatterns = [
    path('vote-post/<int:post_id>/', vote_post, name='vote_post'),
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
    path(
        'subjects/<slug:slug>/',
        views.subject_detail_view,
        name='subject_detail'
    ),
    path('summernote/', include('django_summernote.urls')),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path(
        'comment/<int:pk>/edit/',
        views.edit_comment,
        name='edit_comment'
    ),
    path(
        'comment/<int:pk>/delete/',
        views.delete_comment,
        name='delete_comment'
    ),
    path('resource/<int:pk>/edit/', views.edit_resource, name='edit_resource'),
    path(
        'resource/<int:pk>/delete/',
        views.delete_resource,
        name='delete_resource'
    ),
    path('vote-resource/<int:resource_id>/',
         views.vote_resource,
         name='vote_resource'),

    path('verify-resource/<int:resource_id>/',
         views.verify_resource,
         name='verify_resource'),

    # Home feed URL
    path('', views.index, name='index'),

    # Create Post URL
    path('create/', views.create_post, name='create_post'),

    # Authentication URLs
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
