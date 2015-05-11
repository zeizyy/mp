# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='gender',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mentor',
            name='school',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mentor',
            name='year',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
