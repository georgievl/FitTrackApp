from django import template
from common.choices import DifficultyChoices

register = template.Library()

@register.filter
def difficulty_display(value):
    try:
        return DifficultyChoices(value).label
    except Exception:
        return value
