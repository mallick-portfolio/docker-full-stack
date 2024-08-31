from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Todo(models.Model):
    title= models.CharField(max_length=250, blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EmailQueue(models.Model):
    to = models.CharField(max_length=250, null=False, blank=False)
    from_user = models.CharField(max_length=250, null=True, blank=True)
    cc = models.CharField(max_length=250, null=False, blank=False)
    subject = models.CharField(max_length=250, null=False, blank=False)
    body = models.TextField()
    status = models.BooleanField(default=False)
    attempt = models.IntegerField(default=0)
    