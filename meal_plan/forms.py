from django import forms
from meal_plan.models import MealPlan
from meals.models import Recipe


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = ['day', 'meal_choice', 'recipe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        qs = Recipe.objects.none()

        if self.is_bound and 'meal_choice' in self.data:
            choice = self.data.get('meal_choice')
            if choice:
                qs = Recipe.objects.filter(category__iexact=choice)

        elif self.instance and self.instance.pk:
            qs = Recipe.objects.filter(category__iexact=self.instance.meal_choice)

        self.fields['recipe'].queryset = qs