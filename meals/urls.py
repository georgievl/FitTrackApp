from meals import views
from django.urls import path, include


urlpatterns = [
    path('meals/', include([
        path('', views.RecipeGroupListView.as_view(), name='meals_group_list'),
        path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
        path('group/<slug:group>/', views.RecipeListByGroupView.as_view(), name='recipe_list_by_group'),
        path('<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
        path('<slug:slug>/edit/', views.RecipeUpdateView.as_view(), name='recipe_update'),
        path('<slug:slug>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
    ])),
]