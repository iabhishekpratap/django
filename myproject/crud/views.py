from django.shortcuts import render
from django.shortcuts import redirect 
# we import redirect so we can easily redirect person to perticular url 
# after performing some action like delete or update
from django.shortcuts import get_object_or_404
# get_object_or_404  →  function that tries to get an object from the database
# if it doesn't find it, it raises a 404 error (page not found)


# Create your views here.
from .models import Recipe

# this si default view which read all the data in the database 
# in our case list all the recipe 

def recipe_list(request):
    recipes = Recipe.objects.all() # fetch all the recipe objects from the database
    return render(request, 'crud/list.html', {'recipes': recipes})


def recipe_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')

        Recipe.objects.create(
            name=name,
            description=description
        )
    return render(request, 'crud/create.html')


def recipe_update(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.name = request.POST.get('name')
        recipe.description = request.POST.get('description')
        recipe.save()
        return redirect('crud:recipe_list')
    
    return render(request, 'crud/edit.html', {'recipe': recipe})

def recipe_delete(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.delete()
        return redirect('crud:recipe_list')
    
    return render(request, 'crud/delete.html', {'recipe': recipe})


def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'crud/detail.html', {'recipe': recipe})


