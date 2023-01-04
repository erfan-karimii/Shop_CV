from django import template
from product.models import Product
register = template.Library()

@register.simple_tag
def show_product_property(details,det,arg=None):
    if arg == 'image':
        product = Product.objects.get(id=details[det]['id'])
        return product.image.url
    else:
        return details[det][arg]

@register.simple_tag
def show_price(details,det,count=None):
    size = show_product_property(details,det,'size')
    color = show_product_property(details,det,'color')
    if count:
        count = show_product_property(details,det,'count')
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

