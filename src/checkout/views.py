from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import CreateAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status

from product.models import Product

from .serializers import CheckOutSerializer
from .models import CheckOut, Order


@method_decorator(csrf_exempt, name='dispatch')
class CheckOutCreateAPIView(CreateAPIView):
    """
    Create View to create a checkout with his product orders
    """
    renderer_classes = (JSONRenderer,)
    serializer_class = CheckOutSerializer
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        orders = []
        for product_code, quantity in request.POST.items():
            quantity = int(quantity)
            if quantity > 0 and quantity < 100:
                try:
                    product = Product.objects.get(code=product_code)
                    orders.append(Order(quantity=quantity, product=product))
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)

        # Check if all order are OK and then save
        for order in orders:
            order.save()

        checkout = CheckOut()
        checkout.save()

        try:
            checkout.orders.add(*orders)
            checkout.save()
        except:
            for order in orders:
                order.delete()
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(CheckOutSerializer(instance=checkout).data,
                        status=status.HTTP_201_CREATED)
