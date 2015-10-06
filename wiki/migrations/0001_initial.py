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
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('text', models.TextField(help_text=b'Formatted using ReST')),
                ('is_published', models.BooleanField(default=False, verbose_name=b'Publish?')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Edit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('edited_on', models.DateTimeField(auto_now_add=True)),
                ('summary', models.CharField(max_length=200)),
                ('article', models.ForeignKey(to='wiki.Article')),
                ('editor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-edited_on'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='wiki.Category'),
        ),
    ]
