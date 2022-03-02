from rest_framework import authentication
from recipes.models import Ingredient, Recipe, Steps
from .serializers import IngredientSerializer, RecipeSerializer, StepsSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Recipe.objects.all()


class IngredientViewSet(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ingredient.objects.all()


class StepsViewSet(viewsets.ModelViewSet):
    serializer_class = StepsSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Steps.objects.all()
