from django.shortcuts import render

from basketapp.models import Basket
from furnitureapp.models import Product


def main(request):
    title = 'Магазин'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    products = Product.objects.all()[:3]
    context = {
        'title': title,
        'products': products,
        'basket': basket,
        'basket_count': basket,
    }
    return render(request, 'furniture_online_store/index.html', context)


def contacts(request):
    title = 'Контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,
    }
    return render(request, 'furniture_online_store/contact.html', context)
