from django.shortcuts import render
from furnitureapp.models import ProductCategory


def products(request):
    title = 'Каталог'
    links_menu = ProductCategory.objects.all()
    context = {
        'title': title,
        'links_menu': links_menu,
        # 'same_products': same_products
    }
    return render(request, 'furnitureapp/products.html', context=context)
