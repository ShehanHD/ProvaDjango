# Generated by Django 2.2.3 on 2019-09-10 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotes',
            old_name='fro',
            new_name='frm',
        ),
        migrations.AddField(
            model_name='quotes',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Time'),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]