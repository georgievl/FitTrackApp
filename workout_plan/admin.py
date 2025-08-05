from django.contrib import admin
from workout_plan.models import WorkoutPlan, WorkoutExercise


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
