from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=100, null=False, blank=False)
  memo = models.TextField(blank=True)
  # created = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  date_completed = models.DateTimeField(null=True, blank=True)
  important = models.BooleanField(default=False)

  def __str__(self):
      return f'{self.title} ({self.id})'
