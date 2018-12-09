from django.db import models

from discount.models import Discount


class Product(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    code = models.CharField(
        max_length=10,
        unique=True
    )
    name = models.CharField(
        max_length=25
    )
    price = models.DecimalField(
        default=0,
        max_digits=5,
        decimal_places=2
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='product'
    )

    class Meta:
        ordering = ['code']
        indexes = [
            models.Index(fields=['code'])
        ]

    def __str__(self):
        return 'Product: {} - {}'.format(self.code, self.price)

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super(Product, self).save(*args, **kwargs)
