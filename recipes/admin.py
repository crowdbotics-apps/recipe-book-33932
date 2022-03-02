from django.contrib import admin
from .models import Ingredient, Recipe, Steps

admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Steps)

# Register your models here.
