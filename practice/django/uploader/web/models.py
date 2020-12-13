from django.db import models
from django.utils import timezone
from config.storage_backends import SchemaStorage


class FilePath(models.Model):
    file_id = models.CharField(unique=True, max_length=200)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)


class Document(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()


class SchemaDocument(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=SchemaStorage())
