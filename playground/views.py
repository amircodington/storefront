from django.shortcuts import render
from django.db.models import Q, F
from store.models import Product

def say_hello(request):
    queryset = Product.objects.order_by('unit_price', '-title'),reversed()
    return render(request, 'hello.html',
    {'name': 'Amir', 'products': list(queryset)})
