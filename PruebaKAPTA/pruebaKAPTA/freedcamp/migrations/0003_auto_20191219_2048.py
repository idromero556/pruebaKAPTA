# Generated by Django 2.1.5 on 2019-12-19 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freedcamp', '0002_auto_20191219_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='proyectos',
        ),
        migrations.AddField(
            model_name='mercado',
            name='proyectos',
            field=models.ManyToManyField(blank=True, to='freedcamp.Proyecto'),
        ),
    ]
