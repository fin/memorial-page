# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20150917_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='email',
            field=models.CharField(help_text=b'Give us a way to contact you', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='message',
            field=models.TextField(help_text=b'A private message to partners and family', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='name',
            field=models.CharField(help_text=b'Name, Location would be ideal', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='text',
            field=models.TextField(help_text=b'A story about how he touched you, or anything else you want to share.'),
        ),
    ]
