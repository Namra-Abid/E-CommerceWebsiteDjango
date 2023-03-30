from django import template
register =template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    print(product,cart)
    for id in keys:
        if int(id)==product.id:
            return True
    return False
@register.filter(name='count_in_cart')
def count_in_cart(product,cart):
    keys=cart.keys()
    print(product,cart)
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return False



