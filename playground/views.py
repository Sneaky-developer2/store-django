from django.shortcuts import render
from django.db import connection

# from django.db import transaction
# from django.db.models import Q, F
# from django.db.models.aggregates import Count, Max, Min, Avg, Sum
# from django.db.models import Value, F, Func, Count, ExpressionWrapper
# from django.db.models.functions import Concat
# from django.contrib.contenttypes.models import ContentType

from store.models import *
from tags.models import TaggedItem


def say_hello(request):
    

    return render(request, 'hello.html', {'name': 'Jalal'})


# with connection.cursor() as cursor:
#         cursor.execute()

# with transaction.atomic():
#         order  = Order()
#         order.customer_id = 1
#         order.save()

#         item = OrderItem()
#         item.order = order
#         item.product_id = -1
#         item.quantity = 1
#         item.unit_price = 10
#         item.save()


# collection = Collection(pk=11)
# collection.delete()

# collection.objects.filter(id__gt=5).delete()

# collection = Collection.objects.get(pk=11)
# collection.featured_product = None
# collection.save()

# Collection.objects.filter(pk=11).update(featured_product=None)


# collection = Collection.objects.create(name='a', featured_product_id=1)


#  queryset = Product.objects.all()
#     queryset[0]
#     list(queryset)


# queryset = TaggedItem.objects.get_tags_for(Product, 1)

# dicounted_price = ExpressionWrapper(
#     F('unit_price') * 0.8, output_field=DecimalField())

# queryset = Product.objects.annotate(
#     discounted_price=dicounted_price
# )

# queryset = Customer.objects.annotate(
#     order_count=Count('order')
# )

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
