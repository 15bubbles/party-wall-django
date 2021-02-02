from rest_framework import routers

from inventory.views import DrinkViewSet, FoodViewSet

router = routers.SimpleRouter()
router.register(r"food", FoodViewSet)
router.register(r"drink", DrinkViewSet)
