# Generated by Django 4.0.2 on 2022-02-28 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_alter_employee_chief_alter_employee_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='chief',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='staff.employee', verbose_name='Начальник'),
        ),
    ]
