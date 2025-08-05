from django.db import models


class WeekdayChoices(models.TextChoices):
    MONDAY = 'Monday', 'Monday'
    TUESDAY = 'Tuesday', 'Tuesday'
    WEDNESDAY = 'Wednesday', 'Wednesday'
    THURSDAY = 'Thursday', 'Thursday'
    FRIDAY = 'Friday', 'Friday'
    SATURDAY = 'Saturday', 'Saturday'
    SUNDAY = 'Sunday', 'Sunday'

class DayPlanChoices(models.TextChoices):
    THIRTY_DAYS = "30-Day", "30‑Day Challenge",
    SIXTY_DAYS = "60-Day", "60‑Day Transformation",
    NINETY_DAYS = "90-Day", "90‑Day Champion",
