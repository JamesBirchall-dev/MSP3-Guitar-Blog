"""
URL routing for the blog application.

Maps URLs to view functions.
"""

from django.urls import path, include
from . import views

urlpatterns = [
    # -------------------------------------------------
    # HOME / FEED
    # -------------------------------------------------

    path('', views.index, name='index'),

    # -------------------------------------------------
    # POSTS
    # -------------------------------------------------

    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('create/', views.create_post, name='create_post'),

    # -------------------------------------------------
    # COMMENTS
    # -------------------------------------------------

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

    # -------------------------------------------------
    # RESOURCES
    # -------------------------------------------------

    path(
        'resource/<int:pk>/edit/',
        views.edit_resource,
        name='edit_resource'
    ),
    path(
        'resource/<int:pk>/delete/',
        views.delete_resource,
        name='delete_resource'
    ),
    path(
        'verify-resource/<int:resource_id>/',
        views.verify_resource,
        name='verify_resource'
    ),

    # -------------------------------------------------
    # LIKES
    # -------------------------------------------------

    path(
        'like-post/<int:post_id>/',
        views.like_post,
        name='like_post'
    ),
    path(
        'like-comment/<int:comment_id>/',
        views.like_comment,
        name='like_comment'
    ),
    path(
        'like-resource/<int:resource_id>/',
        views.like_resource,
        name='like_resource'
    ),

    # -------------------------------------------------
    # PROFILE
    # -------------------------------------------------

    path(
        'profile/<str:username>/',
        views.profile_view,
        name='profile'
    ),
    path(
        'profile/edit/',
        views.edit_profile,
        name='edit_profile'
    ),

    # -------------------------------------------------
    # SUBJECTS
    # -------------------------------------------------

    path(
        'subjects/',
        views.subject_list_view,
        name='subject_list'
    ),
    path(
        'subjects/<slug:slug>/',
        views.subject_detail_view,
        name='subject_detail'
    ),

    # -------------------------------------------------
    # AUTHENTICATION
    # -------------------------------------------------

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # -------------------------------------------------
    # AJAX
    # -------------------------------------------------

    path('get-subject-tags/', views.get_subject_tags, name='get_subject_tags'),

    # Summernote editor routes
    path('summernote/', include('django_summernote.urls')),
]
