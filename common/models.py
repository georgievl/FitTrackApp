from django.contrib.auth.models import User
from django.db import models

from common.choices import WeekdayChoices, MealTimeChoices, DayPlanChoices


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    goal = models.ForeignKey('GoalPlan', null=True, on_delete=models.SET_NULL)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    fitness_goal = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=WeekdayChoices)
    title = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.day} Workout"

class WorkoutExercise(models.Model):
    user = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    name = models.CharField(max_length=100)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField(default=60)

    def __str__(self):
        return f"{self.name} ({self.sets}x{self.reps})"

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=WeekdayChoices)
    meal_time = models.CharField(max_length=20, choices=MealTimeChoices)
    recipe = models.ForeignKey('Recipe', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.day} {self.meal_time}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredients = models.TextField()
    instructions = models.TextField()
    calories = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class GoalPlan(models.Model):
    length = models.CharField(max_length=20, choices=DayPlanChoices, unique=True)
    name = models.CharField(max_length=50)            # “Summer Shred,” etc.
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="goals/")  # for dashboard

    def __str__(self):
        return f"{self.length}‑Day: {self.name}"
