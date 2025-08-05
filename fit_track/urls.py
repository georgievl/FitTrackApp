from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('common.urls')),
    path('workout_plan/', include('workout_plan.urls')),
    path('meal_plan/', include('meal_plan.urls')),
    path('workouts/', include('workouts.urls')),
    path('meals/', include('meals.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)