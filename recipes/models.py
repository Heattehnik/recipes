from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='название')
    times_used = models.IntegerField(default=0, verbose_name='Количество использований')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название рецепта')
    products = models.ManyToManyField(Product, through='RecipeProduct', verbose_name='Ингредиенты')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Ингредиент')
    weight_in_grams = models.PositiveIntegerField(verbose_name='Вес в граммах', null=True, blank=True)

    class Meta:
        unique_together = ('recipe', 'product')
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return f'{self.recipe} - {self.product}'

