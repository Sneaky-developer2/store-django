from django.shortcuts import render
from django.db.models import Q, F
from store.models import Collection, Customer, Order, OrderItem, Product


def say_hello(request):
    queryset = Product.objects.select_related('collection').all()

    return render(request, 'hello.html', {'name': 'Jalal', 'products': list(queryset)})
