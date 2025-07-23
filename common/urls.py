from django.urls import path, include
from . import views
from .views import ProfileUpdateView, DashboardView

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('workouts/', include(
        [path('create/', views.create_workout_plan, name="create_workout_plan"),
         path('<int:pk>/', views.WorkoutPlanDetailView.as_view(), name="workout_plan_detail"),
         path('<int:pk>/edit/', views.update_workout_plan, name="update_workout_plan"),
         path('<int:pk>/delete', views.delete_workout_plan, name="delete_workout_plan"),
         ]
    )),
    path('meal/', include(
        [path('create/', views.create_meal_plan, name="create_meal_plan"),
         path('<int:pk>/', views.MealPlanDetailView.as_view(), name="meal_plan_detail"),
         path('<int:pk>/edit', views.update_meal_plan, name='update_meal_plan'),
         path('<int:pk>/delete', views.delete_meal_plan, name='delete_meal_plan'),]
    )),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name='recipe_create'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'),
]