# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0003_message_user_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(related_name='user_to', default=None, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='user_from',
            field=models.ForeignKey(related_name='user_from', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
