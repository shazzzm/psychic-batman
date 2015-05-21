# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0002_auto_20150521_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
