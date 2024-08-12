from queryset_methods.models import Order, OrderItem, ProductCost, Product
from statistics import mean

def get_average_cost_without_product(product, begin, end):
    """Возвращает среднюю стоимость заказов без указанного товара за определенный промежуток времени

    Args:
        product: наименование товара
        begin: начало периода
        end: окончание периода

    Returns: возвращает числовое значение средней стоимости
    """
    excluded_product = Product.objects.get(name=product).id
    oders_with_excluded_product = Order.objects.filter(orderitem__product_id=excluded_product).values('id')
    orders_list = []
    for orders in oders_with_excluded_product:
        orders_list.append(orders.get('id'))

    tmp_query_orderitem = OrderItem.objects.exclude(order_id__in=orders_list).filter(order__date_formation__gte=begin,
                                                                                     order__date_formation__lte=end).values(
        'order_id', 'product_id', 'count', 'order__date_formation')
    res_list = []
    for elem in tmp_query_orderitem:
        SelectedProductCost = ProductCost.objects.get(product_id=elem.get('product_id'),
                                                      end__gte=elem.get('order__date_formation'),
                                                      begin__lt=elem.get('order__date_formation'))
        res_list.append(SelectedProductCost.value * elem.get('count'))

    return mean(res_list)

    #raise NotImplementedError
