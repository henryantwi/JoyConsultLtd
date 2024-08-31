from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('signin/', views.login, name='sign_in'),
    path('signup/', views.sign_up, name='sign_up'),
]
