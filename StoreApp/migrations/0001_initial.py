# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('author', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('rating', models.FloatField(default=3)),
                ('students', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
    ]
