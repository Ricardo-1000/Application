# Generated by Django 3.0.8 on 2020-07-26 17:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 26, 17, 49, 9, 550772, tzinfo=utc)),
        ),
    ]
