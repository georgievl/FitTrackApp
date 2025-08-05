from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'weight', 'height', 'goal']
        widgets = {
            'fitness_goal': forms.TextInput(attrs={
                'rows': 4,
                'class': 'form-control',
                'style': 'resize: vertical;'
            }),
        }

class ChooseGoalForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['goal']
