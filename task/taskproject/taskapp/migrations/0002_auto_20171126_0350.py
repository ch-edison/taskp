# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 03:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='task',
            name='image_width',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Images/NoneU/img.jpg', height_field='image_height', upload_to='Images/', width_field='image_width'),
        ),
    ]