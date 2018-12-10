from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer

from django.shortcuts import get_object_or_404

from .serializers import ProductSerializer
from .models import Product


class ProductListAPIView(ListAPIView):
    """
    List view to get every product
    """
    renderer_classes = (JSONRenderer,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ()


class ProductRetrieveAPIView(RetrieveAPIView):
    """
    Retrieve view to get a product
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = ProductSerializer
    permission_classes = ()

    def get_object(self):
        return get_object_or_404(Product,
                                 code=self.kwargs.get('code').upper())
