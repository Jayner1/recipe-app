from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView

# Create your views here.

def recipes_home(request):
  context = {
    'title': 'Home',
  }
  return render(request, 'recipes_home.html', context)

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'