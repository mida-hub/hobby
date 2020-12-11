from django.db import models
from django.utils import timezone

class FilePath(models.Model):
    file_id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)
