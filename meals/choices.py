from django.db import models


class MealChoiceChoices(models.TextChoices):
    BREAKFAST = 'Breakfast', 'Breakfast'
    LUNCH = 'Lunch', 'Lunch'
    DINNER = 'Dinner', 'Dinner'
    VEGETARIAN = 'Vegetarian', 'Vegetarian'
    BBQ_GRILL = 'BBQ GRILL', 'BBQ GRILL'
    SNACK = 'Snack', 'Snack'
    PROTEIN_SHAKE = 'Protein Shake', 'Protein Shake'