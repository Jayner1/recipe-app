from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView

# Create your views here.

def home(request):
    return render(request, 'recipes/recipes-home.html')

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/recipes-list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        recipe_type = self.request.GET.get('type')
        if recipe_type:
            queryset = queryset.filter(recipe_type=recipe_type)
        return queryset
