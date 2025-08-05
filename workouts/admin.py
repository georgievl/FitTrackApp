from django.contrib import admin
from workouts.models import Exercise


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