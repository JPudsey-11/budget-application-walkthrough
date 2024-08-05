from django.contrib import admin
from .models import project, Expense, category

admin.site.register(Project)
admin.site.register(Expense)
admin.site.register(Category)
