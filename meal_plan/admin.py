from django.contrib import admin
from meal_plan.models import MealPlan


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'meal_choice', 'recipe')
    list_filter = ('day', 'meal_choice')
    search_fields = ('user__username',)
    readonly_fields = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'day', 'meal_choice')}),
        ('Recipe Info', {'fields': ('recipe',)}),
    )