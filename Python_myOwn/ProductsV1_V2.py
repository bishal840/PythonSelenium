products = [
    {'id': 1, 'name': 't-shirt', 'price': '$12.99', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': '$22.45', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': '$43.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': '$14.99', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': '$32.50', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': '$150.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]


for product in products:
    if float(product.get("price")[1:])>25:
        print(product.get("price"))

for product in products:
    if product.get("is_on_sale") and product.get("sale_price") is None:
        print(f"Name: {product.get('name')}")

for product in products:
    if product.get("is_on_sale"):
        print(f"Name: {product.get('name')}. PRICE:{product.get('price')}")