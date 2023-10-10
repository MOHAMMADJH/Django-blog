from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category

# and a new admin registration
# admin.site.register(Post)
# admin.site.register(Category)

from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)


class CategoryInLine(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInLine,]
