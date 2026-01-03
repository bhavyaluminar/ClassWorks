from django.db import models


class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=200)
    instructions = models.TextField()
    cuisine=models.CharField(max_length=200)
    meal_type = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes')
    def __str__(self):
        return self.recipe_name

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
class Review(models.Model):
    recipe=models.ForeignKey(Recipe,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField(default=1,validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipe.recipe_name

