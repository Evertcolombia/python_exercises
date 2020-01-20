#!/usr/bin/python3

#Contact List will inheritance from list class

class ContactList(list):
    def search(self, name):
        """Return all contacts that contain the search value
        in their name"""
        matching_contacts = []

        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    """This class variable will contains the subclass ContactList
    with his methods ans attributes"""
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

c1 = Contact("John A", "jonh@gmail.com")
c2 = Contact("Evert e", "evert@gmail.com")
c3 = Contact("juan j", "juan@gmail.com")

"""To call the function search we use the all_contacts... that 
contains this class definition"""
list_a = [c.name for c in Contact.all_contacts.search('Evert e')]
print(list_a)

print(Contact.all_contacts)
