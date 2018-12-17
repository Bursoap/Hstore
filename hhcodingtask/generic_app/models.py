from django.db import models
from django.contrib.postgres.fields import HStoreField

# Create your models here.


class GenericModel(models.Model):

    name = models.CharField(max_length=50, unique=True)
    data = HStoreField(null=True, blank=True)

    def __str__(self):
        return self.name
