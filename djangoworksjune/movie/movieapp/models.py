from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)

    year = models.IntegerField()

    language = models.CharField(max_length=30)

    image = models.ImageField(upload_to="images")

    description = models.TextField()
