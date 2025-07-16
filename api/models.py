from django.db import models

# Create your models here.
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Poll(models.Model):
    question = models.TextField()
    options = models.JSONField()
    created_by = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

class Vote(models.Model):
    user = models.EmailField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    selected_options = ArrayField(models.IntegerField())  # assuming option index
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'poll')
