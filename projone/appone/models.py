# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ArhProj(models.Model):
    name = models.CharField(max_length=100, unique=True)
    budget = models.IntegerField(default=0)
    description = models.TextField()