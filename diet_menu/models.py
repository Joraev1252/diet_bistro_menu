from uuid import uuid4
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from hitcount.models import HitCount


class CategoriesModel(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return str(self.title)


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "menu/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class MenuModel(models.Model):
    image = models.ImageField(upload_to=upload_location)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    price = models.BigIntegerField()
    category = models.ForeignKey(CategoriesModel, on_delete=models.CASCADE)


    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class PageView(models.Model):
    page = models.CharField(max_length=50, blank=False)
    hits = models.IntegerField(default=0)


class VisitorsModel(models.Model):
    views = models.CharField(max_length=255)

    def __str__(self):
        return str(self.views)