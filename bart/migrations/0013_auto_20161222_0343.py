# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-22 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bart', '0012_auto_20161222_0322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hex_color', models.CharField(blank=True, max_length=7)),
            ],
        ),
        migrations.RemoveField(
            model_name='station',
            name='hex_color',
        ),
        migrations.AddField(
            model_name='station',
            name='lines',
            field=models.ManyToManyField(to='bart.Line'),
        ),
    ]
