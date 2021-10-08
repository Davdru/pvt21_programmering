import requests
import pprint

URL = "https://proagile.se/api/publicEvents"


list_of_courses = requests.get(URL).json()

# list_of_courses innehåller en lista av dictionarys
# varje dictionary representerar en kurs

for course in list_of_courses:
    print(course['courseName'], course['startDate'], course.get('endDate', ""))

