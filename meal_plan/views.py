from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from meal_plan.forms import MealPlanForm
from meal_plan.models import MealPlan
from meals.models import Recipe


@login_required
def create_meal_plan(request):
    meal = MealPlan(user=request.user)

    if request.method == 'POST':
        form   = MealPlanForm(request.POST, instance=meal)
        action = request.POST.get('action')

        if action == 'filter':
            form.fields['recipe'].required = False

        if action == 'save' and form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            messages.success(request, "Meal plan created successfully.")
            return redirect('dashboard')

    else:
        form = MealPlanForm(instance=meal)

    return render(request, 'meal_plan/meal_form.html', {
        'form':      form,
        'title':     'Create Meal Plan',
        'btn_label': 'Add Meal',
    })

class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'meals/recipe_detail.html'

@login_required
def update_meal_plan(request, pk):
    meal = get_object_or_404(MealPlan, pk=pk, user=request.user)

    if request.method == 'POST':
        form   = MealPlanForm(request.POST, instance=meal)
        action = request.POST.get('action')

        if action == 'filter':
            form.fields['recipe'].required = False

        elif action == 'save' and form.is_valid():
            form.save()
            messages.success(request, "Meal plan updated.")
            return redirect('dashboard')

    else:
        form = MealPlanForm(instance=meal)

    return render(request, 'meal_plan/meal_form.html', {
        'form':      form,
        'title':     'Update Meal Plan',
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