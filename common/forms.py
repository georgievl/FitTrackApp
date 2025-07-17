from django import forms
from django.forms import inlineformset_factory

from .models import UserProfile, WorkoutPlan, WorkoutExercise, MealPlan, Recipe


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'weight', 'height', 'fitness_goal', 'goal']
        widgets = {
            'fitness_goal': forms.TextInput(attrs={
                'rows': 4,
                'class': 'form-control',
                'style': 'resize: vertical;'
            }),
        }

class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ['day','title','notes']
    def clean_day(self):
        day = self.cleaned_data['day']
        if WorkoutPlan.objects.filter(user=self.instance.user or self.initial['user'], day=day).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("You already have a plan for this day.")
        return day

WorkoutExerciseFormSet = inlineformset_factory(
    WorkoutPlan,
    WorkoutExercise,
    fields=('name', 'sets', 'reps', 'rest_seconds'),
    extra=1,
    can_delete=True
)

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['name', 'sets', 'reps', 'rest_seconds']

class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['day', 'meal_time', 'recipe']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'calories']

class ChooseGoalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['goal']