s script fetches todos from an API and writes them
to a JSON file
"""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    todos = requests.get(f"{base_url}/todos",
                         timeout=10).json()

    userIds = [todo.get("userId") for todo in todos]

    all_data = {}

    for userId in userIds:
        user = requests.get(f"{base_url}/users/{userId}", timeout=10).json()
        userTodos = requests.get(f"{base_url}/todos?userId={userId}",
                                 timeout=10).json()
        data = [
            {
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed")
            }
            for todo in userTodos
        ]

        all_data[userId] = data

    with open("todo_all_employees.json", "w", encoding='utf-8') as file:
        file.write(json.dumps(all_data, indent=4))
