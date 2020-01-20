#!/usr/bin/python3
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send " 
        "{} order to {}".format(order, self.name))


c = Contact("evert escalante", "evert@gmail.com")
s = Supplier("supli er", "suplier@gmail.com")

print("person: {} {}".format(c.name, c.email))
print("person: {} {}".format(s.name, s.email))
print(c.all_contacts)

s.order("pizza china")

#c.order("pizza china")
