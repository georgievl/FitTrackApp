from django.contrib import admin
from meals.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    search_fields = ('title', 'ingredients')
    fieldsets = (
        (None, {'fields': ('title', 'calories', 'image_url', 'description')}),
        ('Details', {'fields': ('ingredients', 'cooking_instructions')}),
    )
