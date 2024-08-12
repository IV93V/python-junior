from queryset_methods.models import Order, OrderItem, ProductCost
from django.db.models import Sum, Max

def get_top_product_by_total_count_in_period(begin, end):
    tmp_query = OrderItem.objects.filter(order__date_formation__gte=begin, order__date_formation__lte=end).values(
        'product__name', 'product__id', 'count')
    tmp_query_sum = tmp_query.values('product__name', 'product__id').annotate(summ=Sum('count'))
    max_query = tmp_query_sum.aggregate(max_summ=Max('summ'))
    max_value = int(max_query.get('max_summ'))
    max_products_query = tmp_query_sum.filter(summ=max_value)

    res_products = []
    for elem in max_products_query:
        res_products.append((elem.get('product__name'), max_value))

    return res_products
    raise NotImplementedError
