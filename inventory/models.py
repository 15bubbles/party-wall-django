import uuid

from django.db import models


class InventoryItem(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        blank=False,
        null=False,
    )
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=False,
        null=False,
        verbose_name="Price [$]",
    )
    quantity = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    description = models.TextField(
        default="",
        blank=True,
        null=False,
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name} / {self.price}"


class Food(InventoryItem):
    weight = models.FloatField(
        blank=False,
        null=False,
        verbose_name="Weight [g]",
    )

    def __str__(self) -> str:
        return f"Food / {self.name} / {self.weight} / {self.price}"


class Drink(InventoryItem):
    volume = models.FloatField(
        blank=False,
        null=False,
        verbose_name="Volume [ml]",
    )

    def __str__(self) -> str:
        return f"Drink / {self.name} / {self.volume} / {self.price}"
