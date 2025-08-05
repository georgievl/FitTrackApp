from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.text import slugify
from meals.choices import MealChoiceChoices


class Recipe(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image_url = models.ImageField(upload_to='recipes/', blank=True, null=True)
    description = models.TextField(blank=True)
    prep_time = models.PositiveIntegerField(validators=[MaxValueValidator(120)], default=10)
    cook_time = models.PositiveIntegerField(validators=[MaxValueValidator(120)], default=20)
    ingredients = models.TextField()
    calories = models.PositiveIntegerField()
    cooking_instructions = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=MealChoiceChoices,
    )

    @property
    def instruction_steps(self):
        return [line for line in self.cooking_instructions.splitlines() if line.strip()]

    @property
    def ingredient_steps(self):
        return [line for line in self.ingredients.splitlines() if line.strip()]

    slug = models.SlugField(max_length=110, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

