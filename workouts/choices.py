from django.db import models


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