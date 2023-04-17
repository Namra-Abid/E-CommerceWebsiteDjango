from django import template
register =template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys=cart.keys()
    print(product,cart)
    for id in keys:
        #print("cart[id], id :",cart[id], id)
        # if value of product in cart is not zero only then it will return true 
        # we write this condition because 
        # if value of product in cart==0 so it will display - 0 +  
        # which is not good if value is 0 then it should show add to cart button
        value_of_product_in_cart=cart[id]
        if value_of_product_in_cart!=0: 
            if int(id)==product.id:
                return True
    return False
@register.filter(name='count_in_cart')
def count_in_cart(product,cart):
    keys=cart.keys()
    #print(product,cart)
    for id in keys:
        if int(id)==product.id:
            return cart.get(id)
    return False

@register.filter(name='total_price_of_each_product')
def total_price_of_each_product(product,cart):
    return product.price * count_in_cart(product,cart)


@register.filter(name='total_price_of_all_product')
def total_price_of_all_product(AllProductsInCart,cart):
    sum=0
    for p in AllProductsInCart:
        sum=sum+total_price_of_each_product(p,cart)
        #print(sum)
    return sum


@register.filter(name='multiply_any_two_number')
def multiply_any_two_number(number_a,number_b):
    return number_a*number_b
