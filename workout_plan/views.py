from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView
from workout_plan.forms import WorkoutPlanForm, WorkoutExerciseFormSet, WorkoutExerciseFormSetEdit
from workout_plan.models import WorkoutPlan
from workouts.models import Exercise


@login_required
def create_workout_plan(request):

    plan = WorkoutPlan(user=request.user)

    if request.method == 'POST':
        form    = WorkoutPlanForm(request.POST, instance=plan)
        formset = WorkoutExerciseFormSet(request.POST, instance=plan)

        level = None
        if form.is_valid():
            level = form.cleaned_data['workout_type']

        qs = Exercise.objects.filter(experience_level=level) if level else Exercise.objects.none()
        for sub in formset.forms:
            sub.fields['exercise'].queryset = qs

        action = request.POST.get('action')
        if action == 'save' and form.is_valid() and formset.is_valid():
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            formset.instance = plan
            formset.save()
            messages.success(request, "Workout plan created.")
            return redirect('dashboard')

    else:
        form    = WorkoutPlanForm(instance=plan)
        formset = WorkoutExerciseFormSet(instance=plan)

        default_qs = Exercise.objects.filter(
            experience_level=plan.workout_type
        )
        for sub in formset.forms:
            sub.fields['exercise'].queryset = default_qs

    return render(request, 'workout_plan/workout_plan_form.html', {
        'form':    form,
        'formset': formset,
        'title':   'Create Workout Plan',
    })

class WorkoutPlanDetailView(LoginRequiredMixin, DetailView):
    model = WorkoutPlan
    template_name = 'workout_plan/workout_plan_detail.html'

    def get_queryset(self):
        return WorkoutPlan.objects.filter(user=self.request.user)

@login_required
def update_workout_plan(request, pk):
    plan = get_object_or_404(WorkoutPlan, pk=pk, user=request.user)

    form_set = WorkoutExerciseFormSetEdit

    if request.method == 'POST':
        form    = WorkoutPlanForm(request.POST, instance=plan)
        formset = form_set(request.POST, instance=plan)

        if form.is_valid():
            level_qs = Exercise.objects.filter(
                experience_level=form.cleaned_data['workout_type']
            )
            for sub in formset.forms:
                sub.fields['exercise'].queryset = level_qs

        if request.POST.get('action') == 'save' and form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, "Workout plan updated successfully.")
            return redirect('dashboard')
    else:
        form    = WorkoutPlanForm(instance=plan)
        formset = form_set(instance=plan)
        level_qs = Exercise.objects.filter(experience_level=plan.workout_type)
        for sub in formset.forms:
            sub.fields['exercise'].queryset = level_qs

    return render(request, 'workout_plan/workout_plan_form.html', {
        'form':    form,
        'formset': formset,
        'title':   'Edit Workout Plan',
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
