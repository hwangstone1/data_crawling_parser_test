from django.db import models

# Create your models here.


class NewsData(models.Model):

    title = models.CharField(max_length=300)
    link = models.URLField()
    specific_id = models.CharField(max_length=15)

