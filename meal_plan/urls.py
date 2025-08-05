
from django.urls import path, include
from meal_plan import views

urlpatterns = [
    path('meal_plan/', include([
        path('create/', views.create_meal_plan, name='create_meal_plan'),
        path('<int:pk>/', views.MealPlanDetailView.as_view(), name='meal_plan_detail'),
        path('<int:pk>/edit/', views.update_meal_plan, name='update_meal_plan'),
        path('<int:pk>/delete/', views.delete_meal_plan, name='delete_meal_plan'),
    ])),
]