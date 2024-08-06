# budget_application_app/views.py

from django.shortcuts import render, get_object_or_404
from .models import projects

def project_list(request):
    return render(request, 'budget/project-list.html')

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)
    # fetch the correct project
    return render(request, 'budget/project-detail.html', {'project': project, 'expense_list': project.expenses})
