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
]