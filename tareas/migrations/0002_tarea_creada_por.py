# Generated by Django 2.2.24 on 2021-11-17 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tareas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='creada_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tareas_creadas', to=settings.AUTH_USER_MODEL),
        ),
    ]
