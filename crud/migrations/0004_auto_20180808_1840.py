# Generated by Django 2.1 on 2018-08-08 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20180808_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offerservice',
            name='idOffer',
        ),
        migrations.RemoveField(
            model_name='offerservice',
            name='idService',
        ),
        migrations.DeleteModel(
            name='OfferService',
        ),
    ]
