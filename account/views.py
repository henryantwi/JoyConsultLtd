from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        messages.error(request, "Please correct the errors below.")

        ...
    return render(request, "account/login.html")


def sign_up(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        messages.error(request, "Please correct the errors below.")
        ...
    return render(request, 'account/signup.html')
