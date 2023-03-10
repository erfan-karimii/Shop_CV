from django import template
from product.models import Product , Size , Color
# from django.core.exceptions import Do
register = template.Library()


@register.simple_tag
def show_price(id,size,color,discount=None):

    product = Product.objects.get(id=id)
    price_color = 0
    try:

        price_color = product.color_set.get(color=color).Ekhtelaf
    except Color.DoesNotExist:
        pass

    price_size = 0
    try:
        price_size = product.size_set.get(size=size).Ekhtelaf
    except Size.DoesNotExist:
        pass
    

    total_price = price_color + price_size + product.main_discount_call()
    total_price_without_discount = price_color + price_size + product.price
    
    if discount:
        return total_price
    else :
        return total_price_without_discount


