from django.db import models


class Book(models.Model):
    """本モデル"""

    class Meta(object):
        db_table = 'book'

    title = models.CharField(verbose_name='タイトル', max_length=255)
    price = models.PositiveIntegerField(verbose_name='価格', null=True, blank=True)

    def __str__(self):
        return self.title
