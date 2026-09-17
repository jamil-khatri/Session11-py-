def update_cart(cart, item, qty):
    cart[item] = qty
    return cart


cart = {
    "Headphones": 1,
    "Mouse": 2
}

cart = update_cart(cart, "Keyboard", 1)
print(cart)

cart = update_cart(cart, "Mouse", 3)
print(cart)
