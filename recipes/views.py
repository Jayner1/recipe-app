from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('recipes:home')  # Replace 'recipes:home' with the actual URL name of the home page
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')