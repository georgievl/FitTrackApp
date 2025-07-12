from django.urls import path
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
    path('workouts/create/', views.create_workout_plan, name='create_workout_plan'),
    path('workouts/<int:pk>/edit/', views.update_workout_plan, name='update_workout_plan'),
    path('workouts/<int:pk>/delete/', views.delete_workout_plan, name='delete_workout_plan'),
    path('meal/create/', views.create_meal_plan, name='create_meal_plan'),
    path('meal/<int:pk>/edit/', views.update_meal_plan, name='update_meal_plan'),
    path('meal/<int:pk>/delete/', views.delete_meal_plan, name='delete_meal_plan'),
]
