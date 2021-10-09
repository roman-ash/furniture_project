from django.shortcuts import render


def main(request):
    return render(request, 'furniture_online_store/index.html')


def contacts(request):
    return render(request, 'furniture_online_store/contact.html')