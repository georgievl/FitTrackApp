from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from workouts.choices import MuscleGroupChoices, DifficultyChoices


class Exercise(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='exercise/', blank=True, null=True)
    target_muscle_group = models.CharField(max_length=20, choices=MuscleGroupChoices)
    equipment_required = models.CharField(max_length=50)
    experience_level = models.CharField(
        max_length=20,
        choices=DifficultyChoices,
    )
    overview = models.TextField()
    instructions = models.TextField()
    tips = models.TextField()
    slug = models.SlugField(max_length=110, unique=True, blank=True)

    @property
    def overview_steps(self):
        return [line for line in self.overview.splitlines() if line.strip()]

    @property
    def instruction_steps(self):
        return [line for line in self.instructions.splitlines() if line.strip()]

    @property
    def tips_steps(self):
        text = self.tips or ""
        return [line for line in text.splitlines() if line.strip()]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('exercise_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title