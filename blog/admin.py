
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import (
    Subject,
    Profile,
    Post,
    Comment,
    Resource,
    Like,
    Tag,
)


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


class ProfileResource(resources.ModelResource):
    username = resources.Field(column_name='username')

    def dehydrate_username(self, obj):
        return obj.user.username

    class Meta:
        model = Profile
        fields = ('id', 'user', 'username', 'role')


# profile admin
@admin.register(Profile)
class ProfileAdmin(ImportExportModelAdmin):
    resource_class = ProfileResource
    list_display = ('user', 'username', 'role')
    list_filter = ('role',)
    search_fields = ('user__username',)

    def username(self, obj):
        return obj.user.username
    username.short_description = 'Username'

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


# LIKE ADMIN

@admin.register(Like)
class LikeAdmin(ImportExportModelAdmin):
    list_display = ('user', 'post', 'comment', 'resource', 'created_on')
    list_filter = ('created_on',)
