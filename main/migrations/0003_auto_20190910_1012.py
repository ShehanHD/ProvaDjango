# Generated by Django 2.2.3 on 2019-09-10 08:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190910_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 10, 10, 12, 45, 814412), verbose_name='date'),
        ),
    ]