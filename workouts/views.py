from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView
from workouts.forms import ExerciseForm
from workouts.models import Exercise


class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'workouts/exercise_form.html'
    success_url = reverse_lazy('exercise_group_list')

class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'workouts/exercise_list.html'
    context_object_name = 'exercises'

class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = 'workouts/exercise_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class ExerciseUpdateView(LoginRequiredMixin, UpdateView):
    model = Exercise
    form_class = ExerciseForm
    template_name = 'workouts/exercise_form.html'
    slug_field       = 'slug'
    slug_url_kwarg   = 'slug'

    def get_success_url(self):
        return reverse_lazy('exercise_detail', kwargs={'slug': self.object.slug})

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



class ExerciseGroupListView(LoginRequiredMixin, TemplateView):
    template_name = 'workouts/exercise_group_list.html'

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
    template_name = 'workouts/exercise_list.html'
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
    template_name = 'workouts/exercise_form.html'

    def get_initial(self):
        return {
            'target_muscle_group': self.kwargs['group'].replace('-', ' ').title()
        }

    def get_success_url(self):
        return reverse_lazy('exercise_list_by_group', kwargs={'group': self.kwargs['group']})
