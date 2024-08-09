from django.shortcuts import render


def home(request):
    return render(request, "shop/index.html")

def shop(request):
    return render(request, "shop/shop.html")

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
