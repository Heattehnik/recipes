from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Recipe, Product, RecipeProduct
from django.db.models import Q


def add_product_to_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    product_id = request.GET.get('product_id')
    weight = request.GET.get('weight')

    recipe = get_object_or_404(Recipe, id=recipe_id)
    product = get_object_or_404(Product, id=product_id)
    # try:
    recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
    recipe_product.weight_in_grams = weight
    recipe_product.save()
    # except IntegrityError:
    #     return HttpResponse("Рецепт уже содержит указанный рецепт.")

    return HttpResponse("Product added to recipe successfully.")


def cook_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = get_object_or_404(Recipe, id=recipe_id)

    for recipe_product in recipe.recipeproduct_set.all():
        product = recipe_product.product
        product.times_used += 1
        product.save()

    return HttpResponse("Recipe cooked successfully.")


def show_recipes_without_product(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    # Получаем рецепты, без продукта
    recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product)

    # Получаем рецепты, где вес продукта меньше 10 грамм
    recipes_with_low_weight = Recipe.objects.filter(recipeproduct__product=product,
                                                    recipeproduct__weight_in_grams__lt=10)
    # Объединяем результаты
    combined_recipes = (recipes_without_product | recipes_with_low_weight).distinct()
    print(recipes_without_product)
    print(product)

    return render(request, 'recipes/recipes_without_product.html', {'recipes': combined_recipes})

