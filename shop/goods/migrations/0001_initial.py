# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-07 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('ram', models.IntegerField()),
                ('hdd', models.IntegerField()),
                ('date', models.DateField()),
                ('diagonal', models.FloatField()),
                ('weight', models.FloatField()),
                ('wifi', models.BooleanField()),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Cpu')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Good')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('good', models.ManyToManyField(to='goods.Good')),
            ],
        ),
    ]
