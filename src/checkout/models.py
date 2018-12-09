from django.db import models

from product.models import Product
from discount.services import calculate_price_with_discount


class CheckOut(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    orders = models.ManyToManyField(
        'Order'
    )
    total = models.DecimalField(
        default=0,
        max_digits=6,
        decimal_places=2
    )

    class Meta:
        ordering = ['created']

    def __str__(self):
        return 'CheckOut: {} - {}'.format(self.created, self.total)

    def save(self, *args, **kwargs):
        if self.id:
            self.calculate_price()

        super(CheckOut, self).save(*args, **kwargs)

    def calculate_price(self):
        for order in self.orders.all():
            if order.product.discount:
                self.total += calculate_price_with_discount(order)
            else:
                self.total += order.product.price * order.quantity


class Order(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    quantity = models.IntegerField()
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product'
    )

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['product'])
        ]

    def __str__(self):
        return 'Order: {} - {}'.format(self.product.code, self.quantity)
