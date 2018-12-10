from model_mommy import mommy

from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from discount.models import Discount

from .models import Product


class ProductRequestsTestCase(TestCase):
    """
    Class to test product requests
    """
    def setUp(self):
        self.products = mommy.make(Product, _quantity=5)
        self.client = Client()

    def tearDown(self):
        Product.objects.all().delete()
        Discount.objects.all().delete()

    def test_get_all_products_ok(self):
        response = self.client.get(reverse('products_url'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), len(self.products))

    def test_get_product_ok(self):
        response = self.client.get(reverse('product_url', args=[self.products[0].code]))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data['code'], self.products[0].code)