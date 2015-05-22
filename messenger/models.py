from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    message_text = models.TextField()
    time_sent = models.DateTimeField()
    read = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    user_from = models.ForeignKey(User, related_name='user_from')
    user_to = models.ForeignKey(User, related_name='user_to')
