# Generated by Django 3.1.2 on 2020-11-16 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201116_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fooditem',
            old_name='date_ordered',
            new_name='date_created',
        ),
    ]
