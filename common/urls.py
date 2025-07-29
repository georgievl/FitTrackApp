from django.urls import path, include
from common import views
from common.views import ProfileUpdateView, DashboardView

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('workout_plan/', include(
         [path('create/', views.create_workout_plan, name="create_workout_plan"),
         path('<int:pk>/', views.WorkoutPlanDetailView.as_view(), name="workout_plan_detail"),
         path('<int:pk>/edit/', views.update_workout_plan, name="update_workout_plan"),
         path('<int:pk>/delete/', views.WorkoutPlanDeleteView.as_view(), name="delete_workout_plan"),
    ])),
    path('meal_plan/', include([
        path('create/', views.create_meal_plan, name='create_meal_plan'),
        path('<int:pk>/', views.MealPlanDetailView.as_view(), name='meal_plan_detail'),
        path('<int:pk>/edit/', views.update_meal_plan, name='update_meal_plan'),
        path('<int:pk>/delete/', views.delete_meal_plan, name='delete_meal_plan'),
    ])),
    path('meals/', include([
        # path('',                  views.RecipeListView.as_view(),      name='recipe_list'),
        path('', views.RecipeGroupListView.as_view(), name='meals_group_list'),
        path('create/', views.RecipeCreateView.as_view(), name='recipe_create'),
        path('group/<slug:group>/', views.RecipeListByGroupView.as_view(), name='recipe_list_by_group'),
        path('<slug:slug>/',         views.RecipeDetailView.as_view(),    name='recipe_detail'),
        path('<slug:slug>/edit/',    views.RecipeUpdateView.as_view(),    name='recipe_update'),
        path('<slug:slug>/delete/',  views.RecipeDeleteView.as_view(),    name='recipe_delete'),
    ])),
    path('workouts/', include([
        path('', views.ExerciseGroupListView.as_view(), name='exercise_group_list'),
        path('create/', views.ExerciseCreateView.as_view(), name='exercise_create'),
        path('group/<slug:group>/', views.ExerciseListByGroupView.as_view(), name='exercise_list'),
        path('<slug:slug>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
        path('<slug:slug>/edit/', views.ExerciseUpdateView.as_view(), name='exercise_update'),
        path('<slug:slug>/delete/', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
    ])),
]