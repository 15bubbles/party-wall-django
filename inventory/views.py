from rest_framework import viewsets

from inventory.models import Drink, Food
from inventory.serializers import DrinkSerializer, FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filterset_fields = ["name", "price", "quantity", "weight"]
    search_fields = ["@description", "@name"]
    ordering_fields = ["price", "quantity", "weight"]


class DrinkViewSet(viewsets.ModelViewSet):
    queryset = Drink.objects.all()
    serializer_class = DrinkSerializer
    filterset_fields = ["name", "price", "quantity", "volume"]
    search_fields = ["@description", "@name"]
    ordering_fields = ["price", "quantity", "weight"]
