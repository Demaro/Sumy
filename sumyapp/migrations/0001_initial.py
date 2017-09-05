# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 15:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor_nn', models.CharField(blank=True, max_length=20, null=True)),
                ('emisor', models.CharField(blank=True, max_length=20, null=True)),
                ('fecha_inicio', models.DateField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(max_length=10)),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='secretaria', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=20)),
                ('birthdate', models.DateField()),
                ('inicio_cargo', models.DateField(auto_now=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sumyapp.Departamento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
