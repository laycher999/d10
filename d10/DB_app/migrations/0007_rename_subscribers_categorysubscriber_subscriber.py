# Generated by Django 4.2.7 on 2023-11-27 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DB_app', '0006_rename_subscriber_categorysubscriber_subscribers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorysubscriber',
            old_name='subscribers',
            new_name='subscriber',
        ),
    ]
