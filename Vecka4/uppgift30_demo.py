import requests
import datetime
#
#
DAYS = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

# Funktion som tar en textsträng med ett datum
# Som exempelvis 2021-10-15 och ger tillbaks namnet på veckodagen
def date_to_weekday(date_str: str) -> str:
    # Dela upp textsträngen i år månad och dag, m.h.a. split
    year, month, day = date_str.split("-")
    # Skapa ett datumobjekt genom att mata in år, månad och dag
    # datetime.date förväntar sig att dessa skall ges som heltal (int)
    # därför konverterar vi till int
    d = datetime.date(int(year), int(month), int(day))
    # DAYS är en lista som innehåller veckodagarnas namn
    # Måndag med index 0, söndag med index 6
    # d.weekday() ger oss vilken veckodag datumet d infaller på
    # 0 för måndag, 1 för tisdag o.s.v.
    return DAYS[d.weekday()]

# d = datetime.date(2021, 10, 4)
# print(days[d.weekday()])







def print_course(course: dict):
    print(f"Kursnamn: {course['courseName']}, {course['venue']}")
    print(f"Startdatum: {course['startDate']}")
    print(f"Slutdatum: {course.get('endDate', '-')}")
    print(f"Kursen börjar på en: {date_to_weekday(course['startDate'])}")


def main():
    URL = "https://proagile.se/api/publicEvents"
    list_of_courses = requests.get(URL).json()

    year = input("Year>")
    month = input("Month>")

    for course in list_of_courses:
        # Datumen som exempelvis startDate är textsträngar
        # skrivna på formen 2021-10-08 eller År-månad-dag
        course_year, course_month, course_day = course['startDate'].split('-')
        if course_year == year and course_month == month:
            print_course(course)
            print("-" * 80)


if __name__ == '__main__':
    main()

