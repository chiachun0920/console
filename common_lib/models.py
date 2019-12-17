from django.db import models


class Resource(models.Model):
    key = models.CharField(max_length=128)

    value_raw = models.CharField(max_length=1024)

    created_date = models.DateTimeField(auto_now=True)

    updated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key

    class Meta:
        db_table = 'resource'

