# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20161206_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted',
            field=models.DateField(verbose_name='Дата публикации'),
        ),
    ]
