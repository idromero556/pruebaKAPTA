# Generated by Django 2.1.5 on 2019-12-19 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freedcamp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='tareas',
        ),
        migrations.AddField(
            model_name='tarea',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='freedcamp.Proyecto'),
        ),
    ]
