# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanhosts', '0002_auto_20210328_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browseinfo',
            name='user_agent',
            field=models.CharField(default=b'', max_length=255, null=True, verbose_name='\u7528\u6237\u6d4f\u89c8\u5668agent\u4fe1\u606f'),
        ),
    ]
