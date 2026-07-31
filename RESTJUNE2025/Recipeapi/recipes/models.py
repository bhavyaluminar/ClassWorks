from django.db import models
from rest_framework.authtoken.admin import User


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    instructions = models.TextField()
    mealtype = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    image= models.ImageField(upload_to='recipes')

    def __str__(self):
        return self.recipe_name

class Review(models.Model):
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    rating= models.IntegerField()
    created= models.DateField(auto_now_add=True)
    def __str__(self):
        self.recipe.recipe_name
