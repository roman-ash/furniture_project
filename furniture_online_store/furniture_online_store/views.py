from django.shortcuts import render

from basketapp.models import Basket
from furnitureapp.models import Product


def main(request):
    title = 'Магазин'
    products = Product.objects.filter(is_active=True, category__is_active=True).select_related('category')[:3]
    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'furniture_online_store/index.html', context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'furniture_online_store/contact.html', context)
