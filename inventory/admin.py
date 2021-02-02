from django.contrib import admin

from inventory.models import Drink, Food


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    pass


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass
