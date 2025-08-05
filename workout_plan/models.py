from django.contrib.auth import get_user_model
from django.db import models
from common.choices import WeekdayChoices
from workouts.choices import DifficultyChoices
from workouts.models import Exercise


UserModel = get_user_model()

class WorkoutPlan(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.CharField(max_length=9, choices=WeekdayChoices)
    workout_type = models.CharField(
        max_length=20,
        choices=DifficultyChoices,
    )

    def __str__(self):
        return f"{self.user.username} – {self.day} ({self.get_workout_type_display()})"

class WorkoutExercise(models.Model):
    plan = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE, related_name='exercises')
    workout_type = models.CharField(
        max_length=20,
        choices=DifficultyChoices,
    )
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    rest_seconds = models.PositiveIntegerField(default=60)

    def save(self, *args, **kwargs):
        if not self.workout_type and self.plan_id:
            self.workout_type = self.plan.workout_type
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.exercise.title} ({self.sets}×{self.reps})"