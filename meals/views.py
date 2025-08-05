from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView

from meals.choices import MealChoiceChoices
from meals.forms import RecipeForm
from meals.models import Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'meals/recipe_form.html'
    success_url = reverse_lazy('meals_group_list')

class RecipeListView(ListView):
    model = Recipe
    template_name = 'meals/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'meals/recipe_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'meals/recipe_form.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        return reverse_lazy('recipe_detail', kwargs={'slug': self.object.slug})

class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'common/confirm_delete.html'
    success_url = reverse_lazy('meals_group_list')
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Recipe'
        context['cancel_url'] = 'meals_group_list'
        return context

class RecipeGroupListView(LoginRequiredMixin, TemplateView):
    template_name = 'meal_plan/meals_group_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe_groups'] = [
            {'name': label, 'slug': slugify(label)}
            for _, label in MealChoiceChoices.choices
        ]
        return context

class RecipeListByGroupView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'meals/recipe_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        grp = self.kwargs['group'].replace('-', ' ')
        return Recipe.objects.filter(category__iexact=grp)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['group_name'] = self.kwargs['group'].replace('-', ' ').title()
        return ctx
