# Generated by Django 3.0.4 on 2020-05-03 16:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='pub_time'),
        ),
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='pub_date'),
        ),
    ]
