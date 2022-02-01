import requests

# ---------------------------- QUESTION DATA CONFIG ----------------------------
# Amount: max. 50
# Type: "boolean" - True, False/ "multiple" - Multiple Choice, "" - Any
# Difficulty: "easy", "medium", "hard", "" - Any
# Category overview: https://opentdb.com/api_category.php

parameters = {
    "amount": 10,
    "type": "boolean",
    # "difficulty": "hard",
    # "category": 20
}
# ------------------------------------------------------------------------------

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]
