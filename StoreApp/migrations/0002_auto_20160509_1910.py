# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 01:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseapp',
            name='photo',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
        migrations.AlterField(
            model_name='courseapp',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
