# Generated by Django 3.2.8 on 2021-11-02 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_message_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='username',
        ),
    ]