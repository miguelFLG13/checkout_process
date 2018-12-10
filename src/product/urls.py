from django.conf.urls import url

from .views import ProductListAPIView, ProductRetrieveAPIView


urlpatterns = [
    url(r'^(?P<code>[^/]+)/$',
        ProductRetrieveAPIView.as_view(),
        name='product_url'),
    url(r'^$',
        ProductListAPIView.as_view(),
        name='products_url'),
]
