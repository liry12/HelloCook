from django.contrib import admin
from .models import Recipes


class RecipesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]




# Register your models here.
admin.site.register(Recipes, RecipesAdmin)