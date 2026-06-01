similar_movies_data = {

    "101": ["102", "103"],
    "102": ["101", "103"],
    "103": ["101", "102"],

    "201": ["202", "203"],
    "202": ["201", "203"],
    "203": ["201", "202"]
}

def get_similar_movies(movie_id):

    movie_id = str(movie_id)

    if movie_id in similar_movies_data:

        return similar_movies_data[movie_id]

    return []