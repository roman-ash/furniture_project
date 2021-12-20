from django.urls import path
from django.views.decorators.cache import cache_page
from .views import products, product

app_name = 'furnitureapp'

urlpatterns = [
    path('', products, name='main'),
    path('category/<int:pk>', cache_page(3600)(products), name='category'),
    path('product/<int:pk>', cache_page(3600)(product), name='detail'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
]
