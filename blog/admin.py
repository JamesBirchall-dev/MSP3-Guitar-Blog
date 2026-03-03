# Admin configuration for Guitar Learning Blog application.

from django.contrib import admin
from .models import (
    Subject,
    Profile,
    Post,
    Comment,
    Resource,
    Vote,
    Tag,
)
# admin import/export functionality
from import_export.admin import ImportExportModelAdmin


# Subject Admin

@admin.register(Subject)
class SubjectAdmin(ImportExportModelAdmin):

    list_display = ('name', 'slug', 'short_description')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    filter_horizontal = ('tags',)
    fields = ('name', 'slug', 'description', 'short_description', 'tags')


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


# PROFILE ADMIN

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)


# REPLY INLINE (Shows replies inside Post admin)


class ResourceInline(admin.TabularInline):
    model = Resource
    extra = 0


# comment inline (Shows comments inside Post admin)

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


# POST ADMIN

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):

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

    inlines = [CommentInline, ResourceInline]

    filter_horizontal = ('tags',)


# COMMENT ADMIN

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):

    list_display = ('author', 'post', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('content',)


# RESOURCE ADMIN

@admin.register(Resource)
class ResourceAdmin(ImportExportModelAdmin):

    list_display = ('title', 'post', 'added_by', 'created_on')
    search_fields = ('title', 'description')


# VOTE ADMIN

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):

    list_display = ('user', 'post', 'comment', 'created_on')
    list_filter = ('created_on',)
