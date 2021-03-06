# Generated by Django 4.0.3 on 2022-03-05 04:31

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('position', models.CharField(max_length=100, verbose_name='Должность')),
                ('recruitment', models.DateField(verbose_name='Дата приема на работу')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subordinates', to='staff.employee', verbose_name='Начальник')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
