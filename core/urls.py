from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("", include("shop.urls", namespace="shop")),
    path("cart/", include("cart.urls", namespace="cart")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
