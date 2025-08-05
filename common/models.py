from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from common.choices import DayPlanChoices

UserModel = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100, blank=True)
    goal = models.ForeignKey('GoalPlan', null=True, on_delete=models.SET_NULL)
    age = models.PositiveIntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

class GoalPlan(models.Model):
    length = models.CharField(max_length=20, choices=DayPlanChoices, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to="goals/")

    def __str__(self):
        return f"{self.length}‑Day: {self.name}"
