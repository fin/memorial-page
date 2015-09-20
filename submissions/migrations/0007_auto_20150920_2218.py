# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0006_auto_20150920_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='embed',
            field=models.TextField(null=True, blank=True),
        ),
    ]
