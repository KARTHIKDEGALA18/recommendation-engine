from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Recommendation Engine API Running 🔥"}

@app.get("/recommend/{user_id}")
def recommend(user_id: int):
    return {
        "user_id": user_id,
        "recommended_items": [101, 205, 309]
    }
