# budget_application_app/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse  # Corrected import statement
from .models import Project, Category, Expense
from django.views.generic import CreateView
from django.utils.text import slugify
from .forms import ExpenseForm
import json

def project_list(request):
    project_list = Project.objects.all()
    return render(request, 'budget/project-list.html', {'project-list': project_list})

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug=project_slug)

    if request.method == 'GET':
        category_list = Category.objects.filter(project=project)
        return render(request, 'budget/project-detail.html', {'project': project, 'expense_list': project.expenses.all(), 'category_list': category_list})

    elif request.method == 'POST':
        # Process the form
        form = ExpenseForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            amount = form.cleaned_data['amount']
            category_name = form.cleaned_data['category']

            category = get_object_or_404(Category, project=project, name=category_name)

            Expense.objects.create(
                project=project,
                title=title,
                amount=amount,
                category=category
            ).save()
        pass 

    return HttpResponseRedirect(f'/{project_slug}/')

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'budget/add-project.html'
    fields = ('name', 'budget')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.slug = self.generate_unique_slug(self.object.name)
        self.object.save()

        categories = self.request.POST['categoriesString'].split(',')
        for category in categories:
            Category.objects.create(
                project=self.object,
                name=category
            ).save()

        elif request.method == 'DELETE':
            id = json.loads(request.body)['id']
            expense = get_object_or_404(Expense, id=id)
            expense.delete()
        
        return HttpResponse('')


        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return f"/{self.object.slug}/"

    def generate_unique_slug(self, name):
        slug = slugify(name)
        original_slug = slug
        queryset = Project.objects.filter(slug=slug).exists()
        counter = 1
        while queryset:
            slug = f"{original_slug}-{counter}"
            queryset = Project.objects.filter(slug=slug).exists()
            counter += 1
        return slug