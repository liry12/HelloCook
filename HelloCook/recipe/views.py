from django.shortcuts import render, get_object_or_404
from .models import Recipes

# Create your views here.
def recipe_list(request):
    recipes = Recipes.objects.all()
    return render(request, "recipe/recipe_list.html", {"recipes": recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    # recipe = Recipes.objects.get(id=recipe_id)
    pub = recipe.publish
    return render(request, "recipe/recipe_detail.html", {"recipe": recipe, "publish": pub})
