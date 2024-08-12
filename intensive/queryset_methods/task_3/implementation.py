from queryset_methods.models import OrderItem, ProductCost
from itertools import groupby

def get_top_order_by_sum_in_period(begin, end):
    """Возвращает заказ, который имеют наибольшую сумму за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает номер заказа и его сумму
    """

    qs_tmp = OrderItem.objects.filter(order__date_formation__gte='2024-01-01',
                                      order__date_formation__lte='2024-12-01').values('product__id', 'count',
                                                                                      'order__number',
                                                                                      'order__date_formation')
    order_list = []
    for elem in qs_tmp:
        product_cost = ProductCost.objects.get(product=elem.get('product__id'),
                                               begin__lte=elem.get('order__date_formation'),
                                               end__gte=elem.get('order__date_formation')).value
        order_list.append([elem.get('count') * product_cost, elem.get('order__number')])

    order_list_num_group = []
    for num, summ in groupby(order_list, lambda x: x[1]):
        total_summ = sum(x[0] for x in summ)
        order_list_num_group.append([num, total_summ])

    sorted_list = sorted(order_list_num_group, key=lambda x: (x[1], x[0]), reverse=True)
    return (sorted_list[0][0], sorted_list[0][1])

    raise NotImplementedError
