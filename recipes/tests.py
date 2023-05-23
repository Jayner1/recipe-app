from django.test import TestCase
from .models import Recipe

# Create your tests here.

class RecipeModelTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            recipe_name="Test Recipe",
            ingredients="Ingredient 1, Ingredient 2",
            cooking_time="0:30:00",
            difficulty="Easy"
        )

    def test_recipe_name(self):
        self.assertEqual(str(self.recipe.recipe_name), "Test Recipe")

    def test_recipe_ingredients(self):
        self.assertEqual(self.recipe.ingredients, "Ingredient 1, Ingredient 2")

    def test_recipe_cooking_time(self):
        self.assertEqual(str(self.recipe.cooking_time), "0:30:00")

    def test_recipe_difficulty(self):
        self.assertEqual(self.recipe.difficulty, "Easy")

    def test_recipe_type_default_value(self):
        self.assertEqual(self.recipe.recipe_type, "Breakfast")

    def test_recipe_pic_upload_to(self):
        upload_to = Recipe._meta.get_field("pic").upload_to
        self.assertEqual(upload_to, "media/")