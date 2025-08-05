from workouts import views
from django.urls import path, include


urlpatterns = [
    path('workouts/', include([
        path('', views.ExerciseGroupListView.as_view(), name='exercise_group_list'),
        path('create/', views.ExerciseCreateView.as_view(), name='exercise_create'),
        path('group/<slug:group>/', views.ExerciseListByGroupView.as_view(), name='exercise_list'),
        path('<slug:slug>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
        path('<slug:slug>/edit/', views.ExerciseUpdateView.as_view(), name='exercise_update'),
        path('<slug:slug>/delete/', views.ExerciseDeleteView.as_view(), name='exercise_delete'),
    ])),
]