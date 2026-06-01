import json

with open("./data/sample_users.json", "r") as file:
    users_data = json.load(file)

with open("./data/movies.json", "r") as file:
    movies_data = json.load(file)

def get_analytics():

    total_users = len(users_data)

    total_movies = len(movies_data)

    genres = []

    for movie_id in movies_data:

        genre = movies_data[movie_id]["genre"]

        if genre not in genres:
            genres.append(genre)

    return {
        "total_users": total_users,
        "total_movies": total_movies,
        "genres": genres
    }