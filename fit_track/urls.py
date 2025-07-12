from django.contrib import admin
from django.urls import path, include

from common.views import LandingPageView

urlpatterns = [
    path('', include('common.urls')),
    path('admin/', admin.site.urls),
]
