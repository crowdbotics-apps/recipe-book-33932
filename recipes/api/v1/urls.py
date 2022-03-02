from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import IngredientViewSet, RecipeViewSet, StepsViewSet

router = DefaultRouter()
router.register("recipe", RecipeViewSet)
router.register("ingredient", IngredientViewSet)
router.register("steps", StepsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
