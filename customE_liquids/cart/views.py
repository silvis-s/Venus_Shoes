from django.shortcuts import render, redirect
from .cart import Cart
from portfolio.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/autenticacion/login")
def addProd(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect("portfolio")


@login_required(login_url="/autenticacion/login")
def deleteProd(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete(product=product)
    return redirect("portfolio")


@login_required(login_url="/autenticacion/login")
def minusProd(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.minus(product=product)
    return redirect("portfolio")


@login_required(login_url="/autenticacion/login")
def cleanProd(request, product_id):
    cart = Cart(request)
    cart.clean()
    return redirect("portfolio")
