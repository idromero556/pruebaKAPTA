from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('freedcamp/', include(('freedcamp.url', 'freedcamp'),namespace="freedcamp"))
]
