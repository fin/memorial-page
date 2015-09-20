# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_auto_20150919_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='embed',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='name',
            field=models.CharField(help_text=b'<b>Name, Location</b> would be ideal', max_length=200, null=True, blank=True),
        ),
    ]
