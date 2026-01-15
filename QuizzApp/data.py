import requests
import html
def get_questions_data(count):
    """get questions data using API"""
    parameters = {
        "type" : "boolean",
        "amount": count
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    for question in data:
        question["question"] = html.unescape(question["question"])
    return data
