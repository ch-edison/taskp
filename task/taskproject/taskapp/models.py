# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    task_name = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to="Images/",default="Images/NoneU/img.jpg",width_field='image_width', height_field='image_height')
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % self.task_name
