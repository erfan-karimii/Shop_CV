from django import template
from product.models import Product

register = template.Library()

@register.simple_tag
def show(details,det,arg):
    return details[det][arg]

@register.simple_tag
def show_image(details,det):
    x = Product.objects.get(id=details[det]['id'])
    return x.image.url


@register.simple_tag
def show_price(details,det,count=None):
    size = show(details,det,'size')
    color = show(details,det,'color')
    if count:
        count = show(details,det,'count')
    product = Product.objects.get(id=details[det]['id'])
    price_color = 0
    try:
        x = product.color_set.get(color=color)
        price_color = x.Ekhtelaf
    except:
        pass
    price_size = 0
    try:
        x = product.size_set.get(size=size)
        price_size = x.Ekhtelaf
    except:
        pass
    total_price = price_color + price_size + product.main_discount_call()
    if count ==None:
        return total_price
    else:
        return total_price*count


@register.simple_tag
def show_name(details,det):
    x = Product.objects.get(id=details[det]['id'])
    return x.name

@register.simple_tag
def show_count(details,det):
    x = Product.objects.get(id=details[det]['id'])
    return x.product_count


@register.simple_tag
def total_price(details):
    price  = 0
    if details:
        for det in details:
            price += show_price(details,det,'True')
    
    return price