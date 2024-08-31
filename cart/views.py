from decimal import Decimal

from django.http import JsonResponse, HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, render
from icecream import ic

from shop.models import Product

from .cart import Cart


def cart_summary(request: HttpRequest) -> HttpResponse:
    """
    A view to render the cart summary page
    """
    cart: Cart = Cart(request)
    context: dict[str, Cart] = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)


def cart_add(request: HttpRequest) -> JsonResponse:
    """
    Add a product to the cart (qty = 1)
    """
    cart: Cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id: int = int(request.POST.get('productid'))
        product_qty: int = int(request.POST.get('productqty'))
        product: Product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)
        cartqty: int = cart.__len__()
        response: JsonResponse = JsonResponse({'qty': cartqty})
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

        # Get cart details
        cart_qty = cart.__len__()
        cart_subtotal = cart.get_subtotal_price()
        cart_total = cart.get_total_price()

        # Prepare response data
        response_data: dict[str, int | Decimal] = {
            'qty': cart_qty,
            'subtotal': cart_subtotal,
            'total': cart_total,
            'product_id': product_id,
            'product_total_price': product_total_price
        }
        response: JsonResponse = JsonResponse(response_data)
        return response
