# Generated by Django 2.0.3 on 2018-03-16 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mesmerise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
    ]
