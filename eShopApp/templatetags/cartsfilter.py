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


