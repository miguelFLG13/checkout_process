from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from product.models import Product
from checkout.models import Order

from .models import Discount
from .services import calculate_price_with_discount


class CalculatePriceWithDiscountTestCase(TestCase):
    """
    Class to test get products request
    """
    def setUp(self):
        self.discount_1 = Discount(name="2-for-1")
        self.discount_1.save()
        self.discount_2 = Discount(name="3 or more")
        self.discount_2.save()

        self.product_1 = Product(code="TEST1", name="Test 1", price=10, discount=self.discount_1)
        self.product_1.save()
        self.product_2 = Product(code="TEST2", name="Test 2", price=10, discount=self.discount_2)
        self.product_2.save()

        self.order_1 = Order(quantity=5, product=self.product_1)
        self.order_2 = Order(quantity=5, product=self.product_2)

        self.total_1 = 30
        self.total_2 = 45

    def tearDown(self):
        Order.objects.all().delete()
        Product.objects.all().delete()
        Discount.objects.all().delete()

    def test_calculate_price_with_discount_ok(self):
        self.assertEquals(calculate_price_with_discount(self.order_1), self.total_1)
        self.assertEquals(calculate_price_with_discount(self.order_2), self.total_2)