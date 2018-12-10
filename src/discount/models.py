from django.db import models


class Discount(models.Model):
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    name = models.CharField(
        max_length=20
    )

    def __str__(self):
        return 'Discount: {}'.format(self.name)
