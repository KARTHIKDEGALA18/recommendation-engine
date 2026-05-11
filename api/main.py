from fastapi import FastAPI
from services.recommendation_service import get_recommendations

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Recommendation Engine API Running 🔥"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    recommendations = get_recommendations(user_id)

    if recommendations:
        return {
            "user_id": user_id,
            "recommended_items": recommendations
        }

    return {
        "message": "User not found"
    }