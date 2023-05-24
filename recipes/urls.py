from django.urls import path
from .views import home
from .views import RecipeListView
from . import views


app_name = 'recipes'

urlpatterns = [
    path('', views.login_view, name='login'),  # Set login view as the default page
    path('home/', home, name='home'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('login/', views.login_view, name='login'),
    path('breakfasts/', views.breakfasts_view, name='breakfasts'),  # Add URL for breakfasts
    path('lunches/', views.lunches_view, name='lunches'),  # Add URL for lunches
    path('dinners/', views.dinners_view, name='dinners'),  # Add URL for dinners
    path('search/', views.search_view, name='search'),
    path('add-recipe/', views.add_recipe, name='add-recipe'),
    path('about-me/', views.about_me, name='about-me'),

]
