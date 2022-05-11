from django.contrib import admin

from .models import Post, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 3


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Content', {'fields': ['content']}),
        ('Date information', {'fields': ['time_create']})
    ]
    inlines = [CommentInLine]
    list_display = ('title', 'content', 'time_create', 'was_published_recently')
    # filter based on time_create
    list_filter = ['time_create']
    # search based on fields
    search_fields = ['title', 'content']


class CommentAdmin(admin.ModelAdmin):
    fields = ['post', 'comment', 'like']


# Register your mode, ls here.
admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
