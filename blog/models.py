from django.db import models
from django.utils import timezone
from datetime import datetime


class Post(models.Model):  # indicates Post is a django object

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)  # link to another object/model; CASCADE: When the referenced object is deleted, also delete the objects that have references to it
    title = models.CharField(max_length=200)
    text = models.TextField()  # text field without a limit
    created_date = models.DateTimeField(default=datetime.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title