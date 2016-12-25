# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-24 04:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ManyToManyField(to='library.Category'),
        ),
    ]
