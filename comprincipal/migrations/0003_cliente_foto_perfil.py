# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-12 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comprincipal', '0002_auto_20180111_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='foto_perfil',
            field=models.ImageField(default='perfil/generico.png', upload_to='perfil/'),
        ),
    ]
