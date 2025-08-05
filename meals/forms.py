from django import forms
from meals.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title',
                  'image_url',
                  'description',
                  'prep_time',
                  'cook_time',
                  'ingredients',
                  'cooking_instructions',
                  'calories',
                  'category']