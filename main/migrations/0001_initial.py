# Generated by Django 2.2.5 on 2019-09-08 09:31

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='pics/about/default.jpg', upload_to='pics/about')),
                ('timeLine', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='pics/team/default.png', upload_to='pics/team')),
                ('name', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
                ('twiter', models.URLField(blank=True, max_length=256)),
                ('facebook', models.URLField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default='pics/about/default.jpg', upload_to='pics/services')),
                ('day', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 9, 8, 11, 31, 34, 919667), verbose_name='date')),
                ('description', ckeditor.fields.RichTextField(max_length=100)),
                ('state', models.BooleanField(default=True)),
                ('event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.event', verbose_name='Event')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
