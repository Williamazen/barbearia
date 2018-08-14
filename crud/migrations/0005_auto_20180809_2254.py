# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_auto_20180808_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='data_Nasc',
            field=models.DateField(verbose_name='data de nascimento'),
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('DDD', 'num_Tel')]),
        ),
    ]
