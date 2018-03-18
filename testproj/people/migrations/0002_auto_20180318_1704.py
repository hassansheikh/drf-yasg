# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-18 17:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Identity',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='person', to='people.Identity'),
        ),
    ]