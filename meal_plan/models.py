from django.contrib.auth import get_user_model
from django.db import models
from common.choices import WeekdayChoices
from meals.choices import MealChoiceChoices
from meals.models import Recipe


UserModel = get_user_model()

class MealPlan(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=WeekdayChoices)
    meal_choice = models.CharField(max_length=20, choices=MealChoiceChoices)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.day} {self.meal_choice}"
