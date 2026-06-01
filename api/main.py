from fastapi import FastAPI

from services.recommendation_service import get_recommendations
from services.cache_service import (
    get_cached_recommendations,
    set_cached_recommendations
)
from services.analytics_service import get_analytics
from services.similarity_service import get_similar_movies

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Movie Recommendation Engine API Running 🎬"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int, genre: str = None):

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

    if genre:

        filtered_movies = []

        for movie in recommendations:

            if movie["genre"].lower() == genre.lower():
                filtered_movies.append(movie)

        recommendations = filtered_movies

    return {
        "user_id": user_id,
        "recommended_movies": recommendations
    }

@app.get("/analytics")
def analytics():

    return get_analytics()

@app.get("/similar/{movie_id}")
def similar_movies(movie_id: int):

    similar_items = get_similar_movies(movie_id)

    if not similar_items:
        return {
            "error": "Movie not found"
        }

    return {
        "movie_id": movie_id,
        "similar_movies": similar_items
    }