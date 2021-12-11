from django.contrib import admin

# Register your models here.

from myapp.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =["id", "category_name", "created_at", "updated_at"]
    