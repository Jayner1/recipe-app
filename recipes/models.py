from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    TYPE_CHOICES = (
        ('Breakfast', 'Breakfasts'),
        ('Lunch', 'Lunches'),
        ('Dinner', 'Dinners'),
    )

    id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=255)
    ingredients = models.TextField()
    cooking_time = models.CharField(max_length=10)
    difficulty = models.CharField(max_length=50)
    pic = models.ImageField(upload_to='media/', null=True, blank=True)
    recipe_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='Breakfast')
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.recipe_name

