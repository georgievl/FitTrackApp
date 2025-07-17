from django.db import models


class WeekdayChoices(models.TextChoices):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class MealTimeChoices(models.TextChoices):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    SNACK = 'Snack'

class DayPlanChoices(models.TextChoices):
    THIRTY_DAYS = "30-Day", "30‑Day Challenge",
    SIXTY_DAYS = "60-Day", "60‑Day Transformation",
    NINETY_DAYS = "90-Day", "90‑Day Champion",