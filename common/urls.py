from django.urls import path
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
]