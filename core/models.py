from django.db import models
from django.contrib.auth.models import User
from allauth.account.models import user_email


class Message(models.Model):
    msg = models.CharField('Message content', max_length=4)
    username = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.msg
