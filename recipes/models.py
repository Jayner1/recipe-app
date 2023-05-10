from django.db import models

# Create your models here.

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    cooking_time = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.recipe_name