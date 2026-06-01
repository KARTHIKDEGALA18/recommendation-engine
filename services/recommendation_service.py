import json

with open("./data/sample_users.json", "r") as file:
    recommendations_data = json.load(file)

with open("./data/movies.json", "r") as file:
    movies_data = json.load(file)

def get_recommendations(user_id):

    user_id = str(user_id)

    if user_id not in recommendations_data:
        return []

    recommended_movies = []

    for movie_id in recommendations_data[user_id]:

        movie_id = str(movie_id)

        if movie_id in movies_data:

            movie = {
                "id": movie_id,
                "title": movies_data[movie_id]["title"],
                "genre": movies_data[movie_id]["genre"]
            }

            recommended_movies.append(movie)

    return recommended_movies