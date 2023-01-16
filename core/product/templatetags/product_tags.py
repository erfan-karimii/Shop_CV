from django import template
from django.db.models import Avg , Count , Sum
from product.models import Comment , Product
from cart.models import Order, OrderDetail
register = template.Library()


@register.filter(name='_range') 
def _range(number):
    return range(number)

@register.filter(name='average_star') 
def average_star(product_id):
    comments = Comment.objects.filter(is_show=True,product_id=product_id)
    avg_star = comments.aggregate(Avg('point')).get('point__avg')
    resault = avg_star if avg_star is not None else 0
    return  resault

@register.filter(name='sell_count') 
def sell_count(id):
    order = OrderDetail.objects.filter(product_id=id).values_list('orderdetail_count',flat=True)
    order = order.aggregate(Sum('orderdetail_count'))
    return order['orderdetail_count__sum'] if order['orderdetail_count__sum'] is not None else 0


