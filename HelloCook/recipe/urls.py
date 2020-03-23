from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
     path(r'', views.recipe_list, name='recipe_list'),
     path(r'<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
]
