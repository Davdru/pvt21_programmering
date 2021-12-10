import requests
import json

res_data = {"id": "1", "correct": True}
URL = "https://bjornkjellgren.se/quiz/v2/questions"

print(requests.post(URL, json=res_data).text)
