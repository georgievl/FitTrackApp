from django.db import models


class WeekdayChoices(models.TextChoices):
    MONDAY = 'Monday', 'Monday'
    TUESDAY = 'Tuesday', 'Tuesday'
    WEDNESDAY = 'Wednesday', 'Wednesday'
    THURSDAY = 'Thursday', 'Thursday'
    FRIDAY = 'Friday', 'Friday'
    SATURDAY = 'Saturday', 'Saturday'
    SUNDAY = 'Sunday', 'Sunday'

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

class MuscleGroupChoices(models.TextChoices):
    CHEST  = 'Chest',  'Chest'
    ABS    = 'Abs',    'Abs'
    ARMS   = 'Arms',   'Arms'
    LEGS   = 'Legs',   'Legs'
    BACK   = 'Back',   'Back'
    SHOULDERS = 'Shoulders', 'Shoulders'
    CARDIO = 'Cardio','Cardio'