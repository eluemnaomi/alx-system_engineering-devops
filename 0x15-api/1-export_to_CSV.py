s script fetches todos from an API and writes them
to a csv file
"""
import csv
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

    with open(f"{userId}.csv", "w", encoding="utf-8") as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for todo in todos:
            csv_writer.writerow([userId, username, todo.get("completed"),
                                 todo.get("title")])
