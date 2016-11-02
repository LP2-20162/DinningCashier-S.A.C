# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-02 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('razonSocial', models.CharField(max_length=20)),
                ('siglas', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreSuc', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=20)),
                ('telforno', models.CharField(max_length=20)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nivelEmpresa.Empresa')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursals',
            },
        ),
    ]