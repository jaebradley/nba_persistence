# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-23 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='traditionalboxscore',
            old_name='points',
            new_name='plus_minus',
        ),
        migrations.RemoveField(
            model_name='traditionalboxscore',
            name='total_rebounds',
        ),
        migrations.AlterField(
            model_name='game',
            name='nba_id',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('name', 'team', 'jersey_number', 'nba_id')]),
        ),
    ]