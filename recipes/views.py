from django.db import transaction
from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)
    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight_in_grams = weight
    recipe_product.save()

    return HttpResponse("Product added to recipe successfully.")


@transaction.atomic
def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    recipe.recipeproduct_set.all().update(product__times_used=F('product__times_used') + 1)

    return HttpResponse("Recipe cooked successfully.")


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product)
    recipes_with_low_weight = Recipe.objects.filter(recipeproduct__product=product,
                                                    recipeproduct__weight_in_grams__lt=10)
    combined_recipes = (recipes_without_product | recipes_with_low_weight).distinct()
    print(recipes_without_product)
    print(product)

    return render(request, 'recipes/recipes_without_product.html', {'recipes': combined_recipes})

