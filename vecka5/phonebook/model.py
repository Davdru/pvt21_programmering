

class Contact:
    name: str
    phone: str
    email: str

    def __init__(self, name: str, phone: str, email: str):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name}, phone:{self.phone}, email:{self.email}"


class PhoneBook:
    contacts: dict[str: Contact]

    def __init__(self):
        self.contacts = {}

    def add_contact(self, con: Contact):
        self.contacts[con.name] = con

    def get_contact(self, name: str) -> Contact:
        return self.contacts[name]

    def __str__(self):
        res = "Telefonboken\n"
        for contact in self.contacts:
            res += str(self.contacts[contact]) + "\n"
        return res





if __name__ == '__main__':
    c = Contact("Björn Kjellgren", "1234154", "bjorn.kjellgren@kyh.se")
    c2 = Contact("Louise", "123874", "ksjdh@sjdhgfa.com")

    pb = PhoneBook()
    pb.add_contact(c)
    pb.add_contact(c2)

    #print(pb.get_contact("Louise"))
    #print(pb.get_contact("Björn Kjellgren"))
    pb.get_contact("Louise").email = "enbättre@mailadress.se"

    #print(pb.get_contact("Louise"))
    print(pb)
