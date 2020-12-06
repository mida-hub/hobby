from django.db import models

class FilePath(models.Model):
    file_id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=50)
