# Generated by Django 2.2.3 on 2019-09-17 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_remove_quotes_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='quotes',
            name='book',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quotes.book', verbose_name='Book'),
        ),
    ]