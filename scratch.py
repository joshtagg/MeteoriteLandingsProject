import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# prints 10 "todos"
#print(todos[:10])

todos_by_user = {}

for todo in todos:
    if todo["completed"]