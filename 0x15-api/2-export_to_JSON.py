#!/usr/bin/python3
"""
This script fetches todos from an API and writes them
to a JSON file
"""
import json
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get(f"{base_url}/users/{userId}",
                        timeout=10).json()
    todos = requests.get(f"{base_url}/todos?userId={userId}",
                         timeout=10).json()
    username = user.get("username")

    for todo in todos:
        todo['username'] = username

    data = {
        userId: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]
    }

    with open(f"{userId}.json", "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4))
