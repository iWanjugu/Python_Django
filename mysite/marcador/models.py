#encoding: utf-8

# django.contrib.auth - contains the core of the authentication framework, and its default models.
# User - For authenticating users
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# marcador has two models ,Tag' and "Bookmark'
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Meta options: Give additional information or
    # conditions about the models or variables in the models
    class Meta:
        verbose_name = 'tag' # Human readable singular and plural names
        verbose_name_plural = 'tags'
        ordering = ['name'] # ordering will be done using this field

class Bookmark (models.Model):
    url = models.URLField()
    title = models.CharField('title', max_lenth=255)
    description = models.TextField('description' blank=True)
    is_public = models.BooleanField('public', defult=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created'] # why the '-' before date-created????