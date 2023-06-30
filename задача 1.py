import requests
answer = requests.get("https://ru.wikipedia.org/wiki/Python")
print(answer.text.count("Python"))