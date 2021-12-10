

# En kontakt har:
# Förnamn,  efternamn, telefonnummer, epost


# Följande är en klassdefinition
# Den talar om hur en kontakt ser ut
# Vilka attribut, ex förnamn, efternamn
# Vilka metoder som finns. I det här fallet
# print_kontakt och greet
class Kontakt:
    first_name: str # Här talar vi om vilka attribut en Kontakt har och vilken typ
    last_name: str
    phone: str
    email: str

    def __init__(self, f_name, l_name, phone, email):
        # __init__ anropas när vi skapar en ny Kontakt och
        # ansvarar för att attribut sätts på rätt sätt
        # Skriver vi Kontakt('a', 'b', 'c', 'd')
        # kommer __init__ anropas med f_name, l_name etc satta till a, b, c..
        print("I'm in the __init__ method of Kontakt")
        self.first_name = f_name
        self.last_name = l_name
        self.phone = phone
        self.email = email

    # Här definieras en metod, det är något vi kan göra med ett Kontakt-objekt
    # I det här fallet skriva ut datan
    def print_kontakt(self):
        print(f"{self.first_name} {self.last_name}\ntel:{self.phone}\nemail:{self.email} ")

    def greet(self):
        print(f"Hello {self.first_name}")




if __name__ == '__main__':
    k = Kontakt("Björn", "Kjellgren", "12481", "bjorn.kjellgren@kyh.se")
    print(k)

    k.print_kontakt()

    k.phone = "123456789"
    k.print_kontakt()
    k.email = "bjorn.kjellgren@hiq.se"
    k.print_kontakt()
    print("-"*80)
    k2 = Kontakt("Någon", "Annan", "99999999", "en@mail.com")
    k2.print_kontakt()