from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFFICULTY_CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard')
)

class RecipeSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    recipe_name = forms.CharField(label='Recipe Name', max_length=100)
    ingredients = forms.CharField(label='Ingredients', max_length=200)
    cooking_time = forms.IntegerField(label='Cooking Time (minutes)')
    difficulty = forms.ChoiceField(label='Difficulty', choices=DIFFICULTY_CHOICES)
    chart_type = forms.ChoiceField(label='Chart Type', choices=CHART_CHOICES)
