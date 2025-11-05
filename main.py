products=[
    {"name" : "iphone", "price" : 1200},
    {"name" : "macbook", "price" : 2500},
    {"name" : "airpods", "price" : 200},
    {"name" : "ipad", "price" : 900}
]
for product in products:
    if product["price"] <= 1000:
        print(f"{product['name']} ")

for product in products:
    product["price"] *=1.10
    print(f"{product['name']} price is {product['price']}")
sorted_products = sorted(products, key=lambda p: p["price"],reverse=False)
for product in sorted_products:
    print(f"{product['name']} : {product['price']}")
query=input("What would you like to search for? ")
found=False
for product in products:
    if query.lower() in product["name"].lower():
        print(f"Found: {product['name']} at price {product['price']}")
        found=True
        break
if not found:
    print("No products found matching your query.")
new_prod=input("Enter new product name: ")
new_price=float(input("Enter new product price: "))
products.append({"name":new_prod,"price":new_price})
print("Updated product list:")
for product in products:
    print(f"{product['name']} : {product['price']}")

del_prod=input("Enter product name to delete: ")
found = False
for product in products:
    if product["name"].lower() == del_prod.lower():
        products.remove(product)
        found = True
        print(f"{del_prod} has been removed.")
        break
if not found:
    print(f"{del_prod} not found in the product list.")
print("Final product list:")
for product in products:
    print(f"{product['name']} : {product['price']}")