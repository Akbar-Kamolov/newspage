# Generated by Django 4.0.6 on 2022-11-22 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newspage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='photo',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]