from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import TemplateView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from common.forms import UserProfileForm, WorkoutPlanForm, WorkoutExerciseFormSet, MealPlanForm
from common.models import UserProfile, WorkoutPlan, MealPlan


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
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        # Always return the profile for the currently logged-in user
        return UserProfile.objects.get_or_create(user=self.request.user)[0]

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weekday = datetime.now().strftime('%A')  # e.g., 'Wednesday'

        context['today'] = weekday
        context['workout'] = WorkoutPlan.objects.filter(user=self.request.user, day=weekday).first()
        context['meals'] = MealPlan.objects.filter(user=self.request.user, day=weekday).select_related('recipe')

        return context

@login_required
def create_workout_plan(request):
    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST)
        formset = WorkoutExerciseFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            formset.instance = plan
            formset.save()
            return redirect('dashboard')
    else:
        form = WorkoutPlanForm()
        formset = WorkoutExerciseFormSet()

    return render(request, 'common/workout_plan_form.html', {
        'form': form,
        'formset': formset,
    })

from datetime import datetime
from django.shortcuts import render
from .models import WorkoutPlan, MealPlan

@login_required
def dashboard(request):
    today = datetime.today().strftime('%A')  # e.g. "Saturday"

    workout = WorkoutPlan.objects.filter(user=request.user, day=today).first()
    meals = MealPlan.objects.filter(user=request.user, day=today)

    return render(request, 'common/dashboard.html', {
        'today': today,
        'workout': workout,
        'meals': meals,
    })

@login_required
def update_workout_plan(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk, user=request.user)

    if request.method == 'POST':
        form = WorkoutPlanForm(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, "Workout plan updated successfully.")
            return redirect('dashboard')
    else:
        form = WorkoutPlanForm(instance=plan)

    return render(request, 'common/workout_form.html', {
        'form': form,
        'title': 'Update Workout Plan',
        'btn_label': 'Update Plan'
    })

@login_required
def delete_workout_plan(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk, user=request.user)

    if request.method == 'POST':
        plan.delete()
        messages.warning(request, "Workout plan deleted.")
        return redirect('dashboard')

    return render(request, 'common/confirm_delete.html', {
        'object': plan,
        'title': 'Delete Workout Plan',
        'cancel_url': 'dashboard'
    })

@login_required
def create_meal_plan(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            messages.success(request, "Meal plan created successfully.")
            return redirect('dashboard')
    else:
        form = MealPlanForm()

    return render(request, 'common/meal_form.html', {
        'form': form,
        'title': 'Create Meal Plan',
        'btn_label': 'Add Meal'
    })


@login_required
def update_meal_plan(request, pk):
    meal = get_object_or_404(MealPlan, pk=pk, user=request.user)

    if request.method == 'POST':
        form = MealPlanForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            messages.success(request, "Meal plan updated.")
            return redirect('dashboard')
    else:
        form = MealPlanForm(instance=meal)

    return render(request, 'common/meal_form.html', {
        'form': form,
        'title': 'Update Meal Plan',
        'btn_label': 'Save Changes'
    })


@login_required
def delete_meal_plan(request, pk):
    meal = get_object_or_404(MealPlan, pk=pk, user=request.user)

    if request.method == 'POST':
        meal.delete()
        messages.warning(request, "Meal plan deleted.")
        return redirect('dashboard')

    return render(request, 'common/confirm_delete.html', {
        'object': meal,
        'title': 'Delete Meal Plan',
        'cancel_url': 'dashboard'
    })