import requests
import datetime

# Adressen från vilken vi vill hämta data
URL = "https://bjornkjellgren.se/quiz/v1/questions"


# Använd biblioteket requests för att hämta datan och spar i en variabeln result
result = requests.get(URL)


result_json = result.json()

print(result_json)
print(type(result_json))
print(len(result_json))

