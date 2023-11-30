from menu import products

def get_product_by_id(id):

    if not isinstance(id, int):
        raise TypeError("product id must be an int")
     
    for product in products:
        if id == product["_id"]:
            return product
       
        
    return {}  


def get_products_by_type(type_product):

    if not isinstance(type_product, str):
        raise TypeError("product type must be a str")
    
    product_found = []

    for value in products:
        if value["type"] == type_product:
            product_found.append(value)
    return product_found


def add_product(menu, **product):
    if len(menu) == 0:
        product["_id"] = 1
    else:
        bigger_id = max(product.get("_id", 0) for product in menu)
        product["_id"] = bigger_id + 1
    menu.append(product)
    return product   


def menu_report():
    product_count = len(products)
    average_price = round(sum(product["price"] for product in products) / product_count, 2)
    most_common_type = max(set(product["type"] for product in products), key=lambda x: (sum(1 for product in products if product["type"] == x), x))

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {most_common_type}"


