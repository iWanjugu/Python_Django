#encoding: utf-8

# django.contrib.auth - contains the core of the authentication framework, and its default models.
# User - For authenticating users
from django.contrib.auth.models import User
from django.db import models

#https://docs.djangoproject.com/en/1.8/ref/utils/
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now

# Create your models here.
# marcador has two models ,Tag' and "Bookmark'

@python_2_unicode_compatible
#https://docs.djangoproject.com/en/1.8/topics/db/models/
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    # Meta options: Give additional information or
    # conditions about the models or variables in the models
    class Meta:
        #https://docs.djangoproject.com/en/1.8/topics/db/models/#meta-options
        verbose_name = 'tag' # Human readable singular and plural names
        verbose_name_plural = 'tags'
        ordering = ['name'] # ordering will be done using this field

    def __str__(self):
        return self.name


######## Additional Manager that returns public bookmarks only for the mode 'Bookmark'
class PublicBookmarkManager(models.Model):
    def get_queryset(self):
        qs = super(PublicBookmarkManager, self).get_query
        return qs.filer(is_public=True)

@python_2_unicode_compatible
class Bookmark (models.Model):
    url = models.URLField()
    title = models.CharField('title', max_lenth=255)
    description = models.TextField('description' blank=True)
    is_public = models.BooleanField('public', defult=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner', related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)


    objects = models.Manager()
    public = PublicBookmarkManager()

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created'] # why the '-' before date-created????

        def __str__(self):
            return '%s (%s)' % (self.title, self.url)

        def save(self, *args, **kwargs):
            if not self.id:
                self.date_created = now()
            self.date_updated = now()
            super(Bookmark, self).save(*args, **kwargs)