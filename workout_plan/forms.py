from django import forms
from django.forms import inlineformset_factory
from workout_plan.models import WorkoutPlan, WorkoutExercise


class WorkoutPlanForm(forms.ModelForm):
    class Meta:
        model  = WorkoutPlan
        fields = ['day', 'workout_type']

class WorkoutExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutExercise
        fields = ['exercise', 'sets', 'reps', 'rest_seconds']

WorkoutExerciseFormSet = inlineformset_factory(
    parent_model=WorkoutPlan,
    model=WorkoutExercise,
    fields=('exercise', 'sets', 'reps', 'rest_seconds'),
    extra=1,
    can_delete=False,
)

WorkoutExerciseFormSetEdit = inlineformset_factory(
    parent_model=WorkoutPlan,
    model=WorkoutExercise,
    form=WorkoutExerciseForm,
    fields=('exercise','sets','reps','rest_seconds'),
    extra=0,
    can_delete=False,
)
