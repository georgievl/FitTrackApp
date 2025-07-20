from django.contrib import admin
from .models import UserProfile, WorkoutPlan, WorkoutExercise, MealPlan, Recipe, GoalPlan


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height')
    search_fields = ('user__username',)
    readonly_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user',)
        }),
        ('Personal Info', {
            'fields': ('age', 'weight', 'height', )
        }),
    )


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'title')
    list_filter = ('day',)
    search_fields = ('user__username', 'title')
    readonly_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'day', 'title')
        }),
        ('Additional Notes', {
            'fields': ('notes',)
        }),
    )


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sets', 'reps', 'rest_seconds')
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'sets', 'reps', 'rest_seconds')
        }),
    )


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'meal_time', 'recipe')
    list_filter = ('day', 'meal_time')
    search_fields = ('user__username',)
    readonly_fields = ('user',)

    fieldsets = (
        (None, {
            'fields': ('user', 'day', 'meal_time')
        }),
        ('Recipe Info', {
            'fields': ('recipe',)
        }),
    )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    search_fields = ('title', 'ingredients')

    fieldsets = (
        (None, {
            'fields': ('title', 'calories')
        }),
        ('Details', {
            'fields': ('ingredients', 'instructions')
        }),
    )

@admin.register(GoalPlan)
class GoalPlanAdmin(admin.ModelAdmin):
    list_display  = ('name','length')
    list_filter   = ('length',)
    search_fields = ('name',)
    ordering      = ('length',)
