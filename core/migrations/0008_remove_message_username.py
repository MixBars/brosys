# Generated by Django 3.2.8 on 2021-11-02 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_message_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='username',
        ),
    ]
