from django.shortcuts import render

from .models import Product


def home(request):
    return render(request, "shop/index.html")


def shop(request):
    products = Product.objects.all()
    for product in products:
        print(product.image.url)
    return render(request, "shop/shop.html", {"products": products})


def about(request):
    return render(request, "shop/about.html")


def services(request):
    return render(request, "shop/services.html")


def blog(request):
    return render(request, "shop/blog.html")


def contact(request):
    return render(request, "shop/contact.html")


# def account(request):
#     return render(request, "shop/account.html")


def cart(request):
    return render(request, "shop/cart.html")


def checkout(request):
    return render(request, "shop/checkout.html")


def thankyou(request):
    return render(request, "shop/thankyou.html")
    return render(request, "shop/thankyou.html")
