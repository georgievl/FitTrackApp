from collections import OrderedDict
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from common.forms import UserProfileForm
from common.models import UserProfile
from meal_plan.models import MealPlan
from meals.choices import MealChoiceChoices
from workout_plan.models import WorkoutPlan
from workouts.choices import DifficultyChoices


class LandingPageView(TemplateView):
    template_name = 'common/landing.html'

class AboutPageView(TemplateView):
    template_name = 'common/about.html'

class RegisterView(FormView):
    template_name = 'common/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'common/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('landing')

    def dispatch(self, request, *args, **kwargs):
        print("Logout view triggered")
        return super().dispatch(request, *args, **kwargs)

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'common/profile.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        weekday = datetime.now().strftime('%A')

        today_plans = (
            WorkoutPlan.objects
            .filter(user=self.request.user, day=weekday)
            .annotate(ex_count=Count('exercises'))
            .filter(ex_count__gt=0)
            .prefetch_related('exercises__exercise')
        )
        workouts_by_type = OrderedDict()
        for key, label in (
                DifficultyChoices.choices):
            qs = today_plans.filter(workout_type=key)
            if qs.exists():
                workouts_by_type[label] = qs

        today_meals = (
            MealPlan.objects
            .filter(user=self.request.user, day=weekday)
            .select_related('recipe')
        )
        meals_by_choice = OrderedDict()
        for key, label in MealChoiceChoices.choices:
            qs = today_meals.filter(meal_choice=key)
            if qs.exists():
                meals_by_choice[label] = qs

        profile, _ = UserProfile.objects.get_or_create(user=self.request.user)

        ctx.update({
            'today': weekday,
            'workouts_by_type': workouts_by_type,
            'meals_by_choice': meals_by_choice,
            'current_goal': profile.goal,
            'goal_info': self._build_goal_info(profile.goal),
        })
        return ctx

    def _build_goal_info(self, goal):
        if not goal:
            return None
        length = int(goal.length)
        return {
            30: {'weekly_workouts':5,'cheat_days':2,'meals_per_day':5},
            60: {'weekly_workouts':6,'cheat_days':1,'meals_per_day':6},
        }.get(length, {'weekly_workouts':7,'cheat_days':0,'meals_per_day':7})
