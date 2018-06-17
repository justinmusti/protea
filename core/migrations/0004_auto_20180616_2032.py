# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-16 20:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180616_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='conversation',
            name='professional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='professional', to=settings.AUTH_USER_MODEL),
        ),
    ]
