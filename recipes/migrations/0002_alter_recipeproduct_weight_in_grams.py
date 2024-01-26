# Generated by Django 4.2.9 on 2024-01-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeproduct",
            name="weight_in_grams",
            field=models.PositiveIntegerField(
                blank=True, null=True, verbose_name="Вес в граммах"
            ),
        ),
    ]