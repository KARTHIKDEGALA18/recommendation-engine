from fastapi import FastAPI
from services.recommendation_service import get_recommendations
from services.cache_service import (
    get_cached_recommendations,
    set_cached_recommendations
)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Recommendation Engine API Running 🔥"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    cached_data = get_cached_recommendations(user_id)

    if cached_data:
        return {
            "source": "cache",
            "user_id": user_id,
            "recommended_items": cached_data
        }

    recommendations = get_recommendations(user_id)

    if recommendations:

        set_cached_recommendations(user_id, recommendations)

        return {
            "source": "database",
            "user_id": user_id,
            "recommended_items": recommendations
        }

    return {
        "message": "User not found"
    }