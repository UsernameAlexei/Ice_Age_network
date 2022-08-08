from django.db import models
from django.utils import timezone


class News(models.Model):
    url = models.CharField(max_length=250, unique=True)
    content = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['content']
