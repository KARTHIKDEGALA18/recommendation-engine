import json

with open("./data/sample_users.json", "r") as file:
    recommendations_data = json.load(file)

with open("./data/products.json", "r") as file:
    products_data = json.load(file)

def get_recommendations(user_id):

    user_id = str(user_id)

    if user_id not in recommendations_data:
        return []

    recommended_products = []

    for product_id in recommendations_data[user_id]:

        product_id = str(product_id)

        if product_id in products_data:

            product = {
                "id": product_id,
                "name": products_data[product_id]["name"],
                "category": products_data[product_id]["category"]
            }

            recommended_products.append(product)

    return recommended_products