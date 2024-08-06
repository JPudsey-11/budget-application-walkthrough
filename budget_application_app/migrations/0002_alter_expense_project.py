# Generated by Django 4.2.14 on 2024-08-06 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budget_application_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='budget_application_app.project'),
        ),
    ]
