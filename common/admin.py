from django.contrib import admin
from .models import (
    UserProfile, WorkoutPlan, WorkoutExercise,
    MealPlan, Recipe, GoalPlan, Exercise
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height')
    search_fields = ('user__username',)
    readonly_fields = ('user',)
    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Personal Info', {'fields': ('age', 'weight', 'height')}),
    )


@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'day')
    list_filter = ('day',)
    search_fields = ('user__username', 'title')
    readonly_fields = ('user',)
    fieldsets = (
        (None, {'fields': ('user', 'day')}),
    )


@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'sets', 'reps', 'rest_seconds')
    search_fields = ('exercise__title',)
    fieldsets = (
        (None, {'fields': ('plan', 'exercise', 'sets', 'reps', 'rest_seconds')}),
    )


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


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    search_fields = ('title', 'ingredients')
    fieldsets = (
        (None, {'fields': ('title', 'calories', 'image_url', 'description')}),
        ('Details', {'fields': ('ingredients', 'cooking_instructions')}),
    )


@admin.register(GoalPlan)
class GoalPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'length')
    list_filter = ('length',)
    search_fields = ('name',)
    ordering = ('length',)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'target_muscle_group', 'experience_level')
    search_fields = ('title', 'target_muscle_group', 'equipment_required')
    fieldsets = (
        (None, {
            'fields': ('title', 'target_muscle_group', 'equipment_required', 'experience_level')
        }),
        ('Content', {
            'fields': ('overview', 'instructions', 'tips')
        }),
    )
