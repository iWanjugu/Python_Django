# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('is_public', models.BooleanField(verbose_name='public', default=True)),
                ('date_created', models.DateTimeField(verbose_name='date created')),
                ('date_updated', models.DateTimeField(verbose_name='date updated')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='bookmarks', verbose_name='owner')),
            ],
            options={
                'verbose_name_plural': 'bookmarks',
                'verbose_name': 'bookmark',
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='PublicBookmarkManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'tags',
                'verbose_name': 'tag',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=models.ManyToManyField(to='marcador.Tag', blank=True),
        ),
    ]
