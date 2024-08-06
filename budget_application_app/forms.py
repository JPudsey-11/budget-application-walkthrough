from django import forms

class ExpenseForm(forms.form):
    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()
    

