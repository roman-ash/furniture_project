from django.shortcuts import render


def main(request):
    title = 'Магазин'
    context = {
        'title': title,
    }
    return render(request, 'furniture_online_store/index.html', context)


def contacts(request):
    title = 'Контакты'
    context = {
        'title': title,
    }
    return render(request, 'furniture_online_store/contact.html', context)
