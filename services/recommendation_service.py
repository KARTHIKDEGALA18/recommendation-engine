import json

with open("./data/sample_users.json", "r") as file:
    recommendations_data = json.load(file)

def get_recommendations(user_id):

    user_id = str(user_id)

    if user_id in recommendations_data:
        return recommendations_data[user_id]

    return []