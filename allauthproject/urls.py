from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]