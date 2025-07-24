from django.db import models


class WeekdayChoices(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class MealChoiceChoices(models.TextChoices):
    BREAKFAST = 'Breakfast', 'Breakfast'
    LUNCH = 'Lunch', 'Lunch'
    DINNER = 'Dinner', 'Dinner'
    VEGETARIAN = 'Vegetarian', 'Vegetarian'
    BBQ_GRILL = 'BBQ GRILL', 'BBQ GRILL'
    SNACK = 'Snack', 'Snack'
    PROTEIN_SHAKE = 'Protein Shake', 'Protein Shake'

class DayPlanChoices(models.TextChoices):
    THIRTY_DAYS = "30-Day", "30‑Day Challenge",
    SIXTY_DAYS = "60-Day", "60‑Day Transformation",
    NINETY_DAYS = "90-Day", "90‑Day Champion",

class DifficultyChoices(models.TextChoices):
    BEGINNER     = 'Beginner',     'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED     = 'Advanced',     'Advanced'