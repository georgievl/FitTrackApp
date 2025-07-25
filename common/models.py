from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from common.choices import WeekdayChoices, DayPlanChoices, MealChoiceChoices, DifficultyChoices, MuscleGroupChoices

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
    workout_type = models.CharField(
        max_length=20,
        choices=DifficultyChoices,
        default=DifficultyChoices.BEGINNER
    )

    def __str__(self):
        return f"{self.user.username} – {self.day} ({self.get_workout_type_display()})"

class WorkoutExercise(models.Model):
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    workout_type = models.CharField(
        max_length=20,
        choices=DifficultyChoices,
        default=DifficultyChoices.BEGINNER
    )
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField(default=60)

    def save(self, *args, **kwargs):
        if not self.workout_type and self.plan_id:
            self.workout_type = self.plan.workout_type
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.exercise.title} ({self.sets}×{self.reps})"

class MealPlan(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=WeekdayChoices)
    meal_choice = models.CharField(max_length=20, choices=MealChoiceChoices)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.day} {self.meal_choice}"

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

class Exercise(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='exercise/', blank=True, null=True)
    target_muscle_group = models.CharField(max_length=20, choices=MuscleGroupChoices)
    equipment_required = models.CharField(max_length=50)
    experience_level = models.CharField(
        max_length=20,
        choices=DifficultyChoices,
        default=DifficultyChoices.BEGINNER
    )
    overview = models.TextField()
    instructions = models.TextField()
    tips = models.TextField()
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('exercise_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title