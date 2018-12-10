from django.conf.urls import url

from .views import CheckOutCreateAPIView


urlpatterns = [
    url(r'^create/$',
        CheckOutCreateAPIView.as_view(),
        name='create_checkout_url'),
]
