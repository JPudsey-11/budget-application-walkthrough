# budget_application_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='list'),
    path('<slug:project_slug>/', views.project_detail, name='detail'),  # Ensure the slash at the end to avoid ambiguity
]