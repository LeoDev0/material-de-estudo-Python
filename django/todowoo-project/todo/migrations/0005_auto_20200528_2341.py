# Generated by Django 3.0.6 on 2020-05-28 23:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
