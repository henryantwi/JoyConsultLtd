from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from icecream import ic

from shop.models import Product

from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    # ic(type(cart))
    for _ in cart:
        # ic(product := _.product)
        # ic(product.total_price)
        ic(_)
        # ic(dir(_))

    context = {
        'cart': cart,
    }
    ic(cart.get_subtotal_price())
    return render(request, 'cart/cart.html', context)


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        ic("Add View", response)
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)
        cart_qty = cart.__len__()
        cart_subtotal = cart.get_subtotal_price()
        cart_total = cart.get_total_price()
        context = {
            'qty': cart_qty,
            'subtotal': cart_subtotal,
            'total': cart_total,
            'productId': product_id,
        }
        response = JsonResponse(context)
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))

        # Update the cart with the new quantity
        cart.update(product=product_id, qty=product_qty)

        # Calculate the product's total price
        product_price = Decimal(Product.objects.get(id=product_id).price)  # Get product price from the database
        product_total_price = product_price * product_qty
        ic(product_total_price)

        # Get cart details
        cart_qty = cart.__len__()
        cart_subtotal = cart.get_subtotal_price()
        cart_total = cart.get_total_price()

        # Prepare response data
        response_data = {
            'qty': cart_qty,
            'subtotal': cart_subtotal,
            'total': cart_total,
            'product_id': product_id,
            'product_total_price': product_total_price
        }

        response = JsonResponse(response_data)
        ic("Update View", response)
        return response
