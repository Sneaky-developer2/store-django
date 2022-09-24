from django.shortcuts import render
# from django.db.models import Q, F
# from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F, Func, Count, ExpressionWrapper
from django.db.models.functions import Concat

from store.models import Collection, Customer, Order, OrderItem, Product


def say_hello(request):






    # dicounted_price = ExpressionWrapper(
    #     F('unit_price') * 0.8, output_field=DecimalField())

    # queryset = Product.objects.annotate(
    #     discounted_price=dicounted_price
    # )

    queryset = Customer.objects.annotate(
        order_count=Count('order')
    )

    # queryset = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(
    #         ' '), F('last_name'), function='CONCAT')
    # )

    # queryset = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )

    # queryset = Order.objects.aggregate(count=Count('id'))
    # queryset = OrderItem.objects.filter(product__id=1).aggregate(units_sold=Sum('quantity'))
    # queryset = Order.objects.filter(customer_id=1).aggregate(count=Count('id'))
    # queryset = Product.objects.filter(collection__id=3).aggregate(min=Min('unit_price'), avg=Avg('unit_price'),max=Max('unit_price'))

    return render(request, 'hello.html', {'name': 'Jalal', 'products': queryset})
