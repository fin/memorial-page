# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_auto_20150917_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='link_to',
        ),
        migrations.AddField(
            model_name='link',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='link',
            name='link',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='submission',
            name='email',
            field=models.CharField(help_text=b'Give us a way to contact you (not public)', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='message',
            field=models.TextField(help_text=b"If you'd like, leave a private message to partner and family (not public)", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='text',
            field=models.TextField(help_text=b'A story about how he touched you, or anything else you want to share. <small>(markdown formatting available)</small>', blank=True),
        ),
    ]
