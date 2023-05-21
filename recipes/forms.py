from django import forms

CHART__CHOICES = (          #specify choices as a tuple
   ('#1', 'Bar chart'),    # when user selects "Bar chart", it is stored as "#1"
   ('#2', 'Pie chart'),
   ('#3', 'Line chart')
   )

class RecipeSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    recipe_name = forms.CharField(label='Recipe Name', max_length=100)
    ingredients = forms.CharField(label='Ingredients', max_length=200)
    cooking_time = forms.IntegerField(label='Cooking Time (minutes)')
    # Add more fields as needed