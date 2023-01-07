from django import template
from django.db.models import Avg
from product.models import Comment
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