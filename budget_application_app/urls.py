# budget_application_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='list'),
    path('add/', views.ProjectCreateView.as_view(), name='add'),  # Ensure this line is correct
    path('<slug:project_slug>/', views.project_detail, name='detail'),
]