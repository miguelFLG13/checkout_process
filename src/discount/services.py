import math


def calculate_price_with_discount(order):
    """
    Calculate the price of order with a product with a discount

    :param order: a order with discount
    :type order: Order

    :return: order price
    :type: real
    """
    if order.product.discount.id == 1 and order.quantity > 1:
        return ((order.quantity - math.trunc(order.quantity / 2)) *
                order.product.price)
    elif order.product.discount.id == 2 and order.quantity > 2:
        return order.quantity * (order.product.price - 1)
    return order.product.price * order.quantity
