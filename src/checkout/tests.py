import random
from model_mommy import mommy

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from discount.models import Discount
from product.models import Product

from .models import CheckOut, Order


class CheckOutRequestsTestCase(TestCase):
    """
    Class to test create checkout request
    """
    def setUp(self):
        self.products = mommy.make(Product, _quantity=5)
        self.client = Client()

    def tearDown(self):
        Order.objects.all().delete()
        CheckOut.objects.all().delete()
        Product.objects.all().delete()
        Discount.objects.all().delete()

    def test_create_checkout_ok(self):
        payload = {}
        for product in self.products:
            payload[product.code] = random.randint(1, 5)
        response = self.client.post(reverse('create_checkout_url'), payload)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(CheckOut.objects.count(), 1)
        self.assertEquals(Order.objects.count(), 5)