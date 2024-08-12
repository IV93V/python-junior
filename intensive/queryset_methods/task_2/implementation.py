from queryset_methods.models import Customer, Order
from django.db.models import Count

def get_top_customer_in_period(begin, end):
    """Возвращает покупателя, который сделал наибольшее количество заказов за определенный промежуток времени

    Args:
        begin: начало периода
        end: окончание периода

    Returns: возвращает имя покупателя и количество его заказов за указанный период
    """
    qs = Order.objects.filter(date_formation__gte = '2024-01-01', date_formation__lte = '2024-10-10').values('customer__name').annotate(amount=Count("id"))
    ordered_qs = qs.order_by('-amount','customer__name')
    return  (ordered_qs[0].get('customer__name'),ordered_qs[0].get('amount'))
    #raise NotImplementedError
