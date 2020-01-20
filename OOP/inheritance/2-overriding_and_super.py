#!/usr/bin/python3
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

#this class will override the __init__method by using a third argument
#called phone, in thys wy overrriding is altering or replacing a method of the superclass.
#new __init__ method in subclass is automatically called instead of the superclass method
class Friend(Contact):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


#The super() functon method is a way to call code on the parent class, it returns th object as an instanc of th parent class, allowing us to calll the parent method directly

class NewFriend(Contact):
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone
