from django.shortcuts import render

from basketapp.models import Basket
from furnitureapp.models import Product


def main(request):
    title = 'Магазин'
    basket = Basket.objects.filter(user=request.user)
    products = Product.objects.all()[:3]
    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'furniture_online_store/index.html', context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'furniture_online_store/contact.html', context)
