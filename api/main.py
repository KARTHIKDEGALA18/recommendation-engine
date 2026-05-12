from fastapi import FastAPI

from services.recommendation_service import get_recommendations
from services.cache_service import (
    get_cached_recommendations,
    set_cached_recommendations
)
from services.analytics_service import get_analytics
from services.similarity_service import get_similar_products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Recommendation Engine API Running 🔥"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int, category: str = None):

    cached_data = get_cached_recommendations(user_id)

    if cached_data:
        recommendations = cached_data
    else:
        recommendations = get_recommendations(user_id)

        if recommendations:
            set_cached_recommendations(user_id, recommendations)

    if not recommendations:
        return {
            "message": "User not found"
        }

    if category:

        filtered_products = []

        for product in recommendations:

            if product["category"].lower() == category.lower():
                filtered_products.append(product)

        recommendations = filtered_products

    return {
        "user_id": user_id,
        "recommended_items": recommendations
    }

@app.get("/analytics")
def analytics():

    return get_analytics()

@app.get("/similar/{product_id}")
def similar_products(product_id: int):

    similar_items = get_similar_products(product_id)

    return {
        "product_id": product_id,
        "similar_products": similar_items
    }