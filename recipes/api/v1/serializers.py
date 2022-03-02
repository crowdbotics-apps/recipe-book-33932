from rest_framework import serializers
from recipes.models import Ingredient, Recipe, Steps


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Steps
        fields = "__all__"
