# Generated by Django 2.2.24 on 2021-11-08 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grupo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clases', to='grupo.Grupo')),
            ],
        ),
    ]