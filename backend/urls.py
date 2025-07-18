"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path ,include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('api.urls')),
# ]

# backend/urls.py
from django.http import JsonResponse
from django.urls import path, include

def root_view(request):
    return JsonResponse({"message": "API is running 🚀"})

urlpatterns = [
    path('', root_view),  # optional health route
    path('api/', include('api.urls')),  # or your app’s route
]
