similar_products_data = {

    "101": ["102", "103"],
    "102": ["101", "103"],
    "103": ["101", "102"],

    "201": ["202", "203"],
    "202": ["201", "203"],
    "203": ["201", "202"]
}

def get_similar_products(product_id):

    product_id = str(product_id)

    if product_id in similar_products_data:

        return similar_products_data[product_id]

    return []