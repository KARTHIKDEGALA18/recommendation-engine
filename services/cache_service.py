cache = {}

def get_cached_recommendations(user_id):

    return cache.get(str(user_id))

def set_cached_recommendations(user_id, recommendations):

    cache[str(user_id)] = recommendations
