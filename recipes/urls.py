from django.urls import path
from .views import recipes_home
from .views import RecipeListView

app_name = 'recipes'

urlpatterns = [    path('', recipes_home, name='recipes_home'),
                   path('recipes_list/', RecipeListView.as_view(), name='list'),
               ]