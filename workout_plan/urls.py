from workout_plan import views
from django.urls import path, include


urlpatterns = [
    path('workout_plan/', include(
        [path('create/', views.create_workout_plan, name="create_workout_plan"),
         path('<int:pk>/', views.WorkoutPlanDetailView.as_view(), name="workout_plan_detail"),
         path('<int:pk>/edit/', views.update_workout_plan, name="update_workout_plan"),
         path('<int:pk>/delete/', views.WorkoutPlanDeleteView.as_view(), name="delete_workout_plan"),
         ])),
]