# Generated by Django 2.2 on 2019-05-20 08:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20190520_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecolumn',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 20, 8, 20, 45, 514657, tzinfo=utc)),
        ),
    ]