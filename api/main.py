from fastapi import FastAPI
import json

app = FastAPI()

# Load sample recommendation data
with open("./data/sample_users.json", "r") as file:
    recommendations_data = json.load(file)

@app.get("/")
def home():
    return {"message": "Recommendation Engine API Running 🔥"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):

    user_id = str(user_id)

    if user_id in recommendations_data:
        return {
            "user_id": user_id,
            "recommended_items": recommendations_data[user_id]
        }

    return {
        "message": "User not found"
    }