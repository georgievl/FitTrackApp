from django.contrib import admin
from .models import UserProfile, WorkoutPlan, WorkoutExercise, MealPlan, Recipe


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'height')
    search_fields = ('user__username',)

@admin.register(WorkoutPlan)
class WorkoutPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'title')
    list_filter = ('day',)
    search_fields = ('user__username', 'title')

@admin.register(WorkoutExercise)
class WorkoutExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sets', 'reps', 'rest_seconds')


@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('user', 'day', 'meal_time', 'recipe')
    list_filter = ('day', 'meal_time')
    search_fields = ('user__username',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'calories')
    search_fields = ('title', 'ingredients')
