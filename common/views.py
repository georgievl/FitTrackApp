from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.text import slugify
from django.views.generic import TemplateView, FormView, UpdateView, DetailView, DeleteView, ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from common.forms import UserProfileForm, WorkoutPlanForm, WorkoutExerciseFormSet, MealPlanForm, RecipeForm, ExerciseForm
from common.models import UserProfile, WorkoutPlan, MealPlan, Recipe, Exercise


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
        context = super().get_context_data(**kwargs)
        weekday = datetime.now().strftime('%A')
        context['today']        = weekday
        context['workouts']     = WorkoutPlan.objects.filter(user=self.request.user, day=weekday)
        context['meals']        = MealPlan.objects.filter(user=self.request.user, day=weekday)
        context['current_goal'] = self.request.user.userprofile.goal

        goal_info = None
        if context['current_goal']:
            length = int(context['current_goal'].length)
            if length == 30:
                goal_info = {
                    'weekly_workouts': 5,
                    'cheat_days': 2,
                    'meals_per_day': 5,
                }
            elif length == 60:
                goal_info = {
                    'weekly_workouts': 6,
                    'cheat_days': 1,
                    'meals_per_day': 6,
                }
            else:
                goal_info = {
                    'weekly_workouts': 7,
                    'cheat_days': 0,
                    'meals_per_day': 7,
                }
        context['goal_info'] = goal_info

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
            messages.success(request, "Workout plan created successfully.")
            return redirect('dashboard')
    else:
        form = WorkoutPlanForm()
        formset = WorkoutExerciseFormSet()

    return render(request, 'common/workout_plan_form.html', {
        'form': form,
        'formset': formset,
        'title': 'Create Workout Plan',
        'btn_label': 'Create Workout Plan',
    })

class WorkoutPlanDetailView(LoginRequiredMixin, DetailView):
    model = WorkoutPlan
    template_name = 'common/workout_plan_detail.html'

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)

@login_required
def update_workout_plan(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk, user=request.user)
    if request.method == 'POST':
        form    = WorkoutPlanForm(request.POST, instance=plan)
        formset = WorkoutExerciseFormSet(request.POST, instance=plan)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Workout plan updated successfully.")
            return redirect('dashboard')
    else:
        form    = WorkoutPlanForm(instance=plan)
        formset = WorkoutExerciseFormSet(instance=plan)

    return render(request, 'common/workout_plan_form.html', {
        'form':      form,
        'formset':   formset,
        'title':     'Edit Workout Plan',
        'btn_label': 'Save Changes',
    })

class WorkoutPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkoutPlan
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']      = 'Delete Workout Plan'
        context['cancel_url'] = 'dashboard'
        return context

class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'common/exercise_form.html'
    success_url = reverse_lazy('exercise_group_list')

class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'common/exercise_list.html'
    context_object_name = 'exercises'

class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = 'common/exercise_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'common/exercise_form.html'
    slug_field       = 'slug'
    slug_url_kwarg   = 'slug'

    def get_success_url(self):
        return reverse_lazy('exercise_detail', kwargs={'slug': self.object.pk})

class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'common/confirm_delete.html'
    slug_field       = 'slug'
    slug_url_kwarg   = 'slug'
    success_url = reverse_lazy('exercise_group_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Exercise'
        context['cancel_url'] = 'exercise_group_list'
        return context

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

class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'common/recipe_detail.html'

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
        'cancel_url': 'dashboard',
    })

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'common/recipe_form.html'
    success_url = reverse_lazy('recipe_list')
class RecipeListView(ListView):
    model = Recipe
    template_name = 'common/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'common/recipe_detail.html'

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'common/recipe_form.html'
    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'pk': self.object.pk})

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('recipe_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Recipe'
        context['cancel_url'] = 'recipe_list'
        return context

class ExerciseGroupListView(LoginRequiredMixin, TemplateView):
    template_name = 'common/exercise_group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        raw = ['Chest', 'Abs', 'Arms', 'Legs', 'Back', 'Shoulders', 'Cardio']
        context['muscle_groups'] = [
            {'name': g, 'slug': slugify(g)}
            for g in raw
        ]
        return context

class ExerciseListByGroupView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'common/exercise_list.html'
    context_object_name = 'exercises'

    def get_queryset(self):
        grp = self.kwargs['group'].replace('-', ' ')
        return Exercise.objects.filter(target_muscle_group__iexact=grp)

    def get_context_data(self, **kw):
        context = super().get_context_data(**kw)
        context['group_name'] = self.kwargs['group'].replace('-', ' ').title()
        return context

class ExerciseCreateByGroupView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'common/exercise_form.html'

    def get_initial(self):
        return {
            'target_muscle_group': self.kwargs['group'].replace('-', ' ').title()
        }

    def get_success_url(self):
        return reverse_lazy('exercise_list_by_group', kwargs={'group': self.kwargs['group']})