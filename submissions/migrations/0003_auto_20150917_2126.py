# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_submission_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='user',
        ),
        migrations.AddField(
            model_name='submission',
            name='name',
            field=models.TextField(null=True, blank=True),
        ),
    ]
