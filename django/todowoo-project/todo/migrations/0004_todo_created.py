# Generated by Django 3.0.6 on 2020-05-28 23:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_todo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
