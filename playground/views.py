from django.shortcuts import render
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F, Func

from store.models import Collection, Customer, Order, OrderItem, Product


def say_hello(request):
    queryset = Customer.objects.annotate(
        full_name=Func(F('first_name'), F('last_name'))
    )




    # queryset = Order.objects.aggregate(count=Count('id'))
    # queryset = OrderItem.objects.filter(product__id=1).aggregate(units_sold=Sum('quantity'))
    # queryset = Order.objects.filter(customer_id=1).aggregate(count=Count('id'))
    # queryset = Product.objects.filter(collection__id=3).aggregate(min=Min('unit_price'), avg=Avg('unit_price'),max=Max('unit_price'))
    return render(request, 'hello.html', {'name': 'Jalal', 'products': queryset})
