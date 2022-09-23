from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from store.models import Collection, Customer, Order, OrderItem, Product





def say_hello(request):
    queryset = Order.objects.filter(customer__id=1)


    return render(request, 'hello.html', {'name': 'Jalal', 'products': list(queryset)})
