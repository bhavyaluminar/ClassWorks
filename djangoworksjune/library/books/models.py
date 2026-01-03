from django.db import models

# Create your models here.
class Book(models.Model):  #table definition

    title=models.CharField(max_length=30)

    author=models.CharField(max_length=30)

    price=models.IntegerField()

    pages=models.IntegerField()

    language=models.CharField(max_length=30)

    image=models.ImageField(upload_to="images")




