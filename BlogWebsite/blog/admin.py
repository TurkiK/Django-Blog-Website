from django.contrib import admin
from .models import User
from .models import Category
from .models import Post
from .models import Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email")


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "date_published")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "date_posted")


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
