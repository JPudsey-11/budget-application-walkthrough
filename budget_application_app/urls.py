# budget_application_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
]