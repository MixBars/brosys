# Generated by Django 3.2.8 on 2021-11-02 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_message_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='username',
            field=models.CharField(default=None, max_length=50, verbose_name='Username'),
            preserve_default=False,
        ),
    ]
