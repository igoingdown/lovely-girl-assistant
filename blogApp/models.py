# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    abstract = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)


class HistoryMessage(models.Model):
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    body = models.CharField(max_length=200)
    url_body = models.CharField(max_length=400, blank=True)
    type = models.IntegerField(blank=True, default=10000)
    talk_direction = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.abstract
