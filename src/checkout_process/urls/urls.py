from django.conf.urls import include, url
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="home.html")),
    url('api/v1/product/', include('product.urls')),
    url('api/v1/checkout/', include('checkout.urls')),
]
