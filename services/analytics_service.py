import json

with open("./data/sample_users.json", "r") as file:
    users_data = json.load(file)

with open("./data/products.json", "r") as file:
    products_data = json.load(file)

def get_analytics():

    total_users = len(users_data)

    total_products = len(products_data)

    categories = []

    for product_id in products_data:

        category = products_data[product_id]["category"]

        if category not in categories:
            categories.append(category)

    return {
        "total_users": total_users,
        "total_products": total_products,
        "categories": categories
    }
    