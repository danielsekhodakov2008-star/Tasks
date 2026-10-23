products = {
    "apple": 10,
    "banana": 3,
    "milk": 7,
    "bread": 2,
    "cheese": 6
}

print("Початкові продукти:", products)

def update_product(name, quantity):
    if name in products:
        products[name] += quantity
    else:
        products[name] = quantity


update_product("apple", 5)
update_product("banana", -1)
update_product("bread", -1)

print("Оновлені продукти:", products)

less_than_5 = []

for product in products:
    if products[product] < 5:
        less_than_5.append(product)

print("Продукти, яких менше 5", less_than_5)
