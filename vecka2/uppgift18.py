people = {
    "Björn": "0445654653",
    "Olof": "123456789",
    "Lisa": "9999999999",
    "Bodil": "555-666-789"
}

# Hämta ett värde baserat på nyckel
print(people["Björn"])

# Kontrollera om nyckel finns i dict
print("Björn" in people)
print("Louise" in people)


# Lägga till en nyckel och värde
people["Louise"] = 1029847
#print(people)

# Hämta telefonnummer för den nya personen
print(people["Louise"])


people["Louise"] = 99999
print(people["Louise"])


del people["Louise"]

print(people)
print(len(people))

# vem = input("Vem vill  du ringa?")
# if vem not in people:
#     print("Sorry hörru, vet ej vem detta är.")
# else:
#     number = people[vem]
#     print(f"Numret till {vem} är {number}")



