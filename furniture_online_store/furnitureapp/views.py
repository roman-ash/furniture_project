from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from basketapp.models import Basket
from furnitureapp.models import ProductCategory, Product
import random


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None, page=1):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            products = Product.objects.filter(quantity__gte=1).order_by('price')  # filter(is_active=True, category__is_active=True) !!OperationalError at/products/ no such column: furnitureapp_product.created
            category = {'pk': 0, 'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk, quantity__gte=1).order_by('price')  # filter(is_active=True, category__is_active=True)
        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator,
        }
        return render(request, 'furnitureapp/products.html', context)
    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)
    products = Product.objects.filter(quantity__gte=1).order_by('price')  # filter(is_active=True, category__is_active=True)

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'products': products,
    }
    return render(request, 'furnitureapp/products.html', context)


def product(request, pk):
    title = 'Детали'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': product,
        'same_products': get_same_products(product),
    }
    return render(request, 'furnitureapp/product.html', context)
