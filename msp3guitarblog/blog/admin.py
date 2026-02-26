# Admin configuration for Guitar Learning Blog application.

from django.contrib import admin
from .models import (
    Subject,
    Profile,
    Post,
    Reply,
    Resource,
    Vote
)


# Subject Admin

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# PROFILE ADMIN

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'role')
    list_filter = ('role',)


# REPLY INLINE (Shows replies inside Post admin)

class ReplyInline(admin.TabularInline):
    model = Reply
    extra = 0


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0


# POST ADMIN

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'author',
        'subject',
        'min_level',
        'status',
        'created_on'
    )

    list_filter = (
        'status',
        'min_level',
        'subject',
        'created_on'
    )

    search_fields = ('title', 'content')

    prepopulated_fields = {'slug': ('title',)}

    date_hierarchy = 'created_on'

    inlines = [ReplyInline, ResourceInline]


# REPLY ADMIN

@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):

    list_display = ('author', 'post', 'is_verified', 'created_on')
    list_filter = ('is_verified', 'created_on')
    search_fields = ('content',)


# RESOURCE ADMIN

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = ('title', 'post', 'added_by', 'created_on')
    search_fields = ('title', 'description')


# VOTE ADMIN

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):

    list_display = ('user', 'post', 'reply', 'created_on')
    list_filter = ('created_on',)
