from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from common.choices import WeekdayChoices, MealTimeChoices, DayPlanChoices

UserModel = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    goal = models.ForeignKey('GoalPlan', null=True, on_delete=models.SET_NULL)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class WorkoutPlan(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
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
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=WeekdayChoices)
    meal_time = models.CharField(max_length=20, choices=MealTimeChoices)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.day} {self.meal_time}"

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.ImageField(upload_to='recipes/', blank=True, null=True)
    description = models.TextField(blank=True)
    prep_time = models.PositiveIntegerField(validators=[MaxValueValidator(120)], default=10)
    cook_time = models.PositiveIntegerField(validators=[MaxValueValidator(120)], default=20)
    ingredients = models.TextField()
    calories = models.PositiveIntegerField()
    cooking_instructions = models.TextField()

    def __str__(self):
        return self.title

class GoalPlan(models.Model):
    length = models.CharField(max_length=20, choices=DayPlanChoices, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="goals/")

    def __str__(self):
        return f"{self.length}‑Day: {self.name}"
