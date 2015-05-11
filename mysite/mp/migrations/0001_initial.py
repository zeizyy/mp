# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=True)),
                ('year', models.IntegerField()),
                ('school', models.IntegerField(max_length=40)),
                ('home', models.CharField(max_length=30)),
                ('high', models.CharField(max_length=20)),
                ('major', models.CharField(max_length=40)),
                ('work', models.CharField(max_length=200)),
                ('intro', models.CharField(max_length=2000)),
                ('ec', models.CharField(max_length=2000)),
                ('hobby', models.CharField(max_length=2000)),
                ('three', models.CharField(max_length=40)),
                ('clas', models.CharField(max_length=1000)),
                ('music', models.CharField(max_length=1000)),
                ('movie', models.CharField(max_length=1000)),
                ('book', models.CharField(max_length=1000)),
                ('quote', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
