# Generated by Django 2.2.3 on 2019-09-10 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20190910_1011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='time',
        ),
    ]
