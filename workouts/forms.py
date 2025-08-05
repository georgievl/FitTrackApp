from django import forms
from workouts.models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            'title',
            'image',
            'target_muscle_group',
            'equipment_required',
            'experience_level',
            'overview',
            'instructions',
            'tips',
        ]