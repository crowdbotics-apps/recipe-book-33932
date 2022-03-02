from django.conf import settings
from django.db import models


class Recipe(models.Model):
    "Generated Model"
    recipe_name = models.BooleanField()
    prep_time = models.IntegerField()
    cook_time = models.IntegerField(
        null=True,
        blank=True,
    )
    servings = models.IntegerField(
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )


class Ingredient(models.Model):
    "Generated Model"
    ingredient = models.CharField(
        max_length=256,
    )
    qty = models.DecimalField(
        max_digits=30,
        decimal_places=2,
    )
    unit = models.CharField(
        max_length=256,
    )
    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="ingredient_recipe",
    )


class Steps(models.Model):
    "Generated Model"
    recipe = models.ForeignKey(
        "recipes.Recipe",
        on_delete=models.CASCADE,
        related_name="steps_recipe",
    )
    step_number = models.IntegerField()
    step_text = models.TextField()


# Create your models here.
