from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes-home.html')

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes-list.html'
