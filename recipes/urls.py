from django.urls import path
from .views import home
from .views import RecipeListView

app_name = 'recipes'

urlpatterns = [    path('', home, name='home'),
                   path('recipes_list/', RecipeListView.as_view(), name='list'),
               ]