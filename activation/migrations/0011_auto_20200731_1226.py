# Generated by Django 3.0.8 on 2020-07-31 09:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0010_auto_20200731_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 9, 26, 6, 707626, tzinfo=utc)),
        ),
    ]
