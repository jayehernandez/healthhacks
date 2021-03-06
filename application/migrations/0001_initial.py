# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=50)),
                ('availability', models.BooleanField()),
                ('ambulance', models.BooleanField()),
                ('location', models.TextField()),
                ('city', models.TextField()),
                ('contactno', models.TextField()),
            ],
        ),
    ]
