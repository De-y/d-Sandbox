from django.urls import path, include 
from .views import IndexView, appView
from django.contrib import admin

urlpatterns = [
    path('', IndexView.as_view(template_name='index.html'), name='home'),
    path('app/', appView.as_view(), name='app'),
    path("service/", include("django.contrib.auth.urls")),  # new
]
