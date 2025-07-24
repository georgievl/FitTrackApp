from django import forms
from django.forms import inlineformset_factory

from .models import UserProfile, WorkoutPlan, WorkoutExercise, MealPlan, Recipe, Exercise


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'weight', 'height', 'goal']
        widgets = {
            'fitness_goal': forms.TextInput(attrs={
                'rows': 4,
                'class': 'form-control',
                'style': 'resize: vertical;'
            }),
        }

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model  = WorkoutPlan
        fields = ['day', 'workout_type']

WorkoutExerciseFormSet = inlineformset_factory(
    parent_model=WorkoutPlan,
    model=WorkoutExercise,
    fields=('exercise', 'sets', 'reps', 'rest_seconds'),
    extra=1,
    can_delete=True,
)

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'rest_seconds']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['day', 'meal_choice', 'recipe']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'image_url', 'description', 'prep_time', 'cook_time', 'ingredients', 'cooking_instructions', 'calories']

class ChooseGoalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['goal']

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