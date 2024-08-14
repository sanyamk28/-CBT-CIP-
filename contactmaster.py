class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f"Contact(Name: {self.name}, Phone: {self.phone}, Email: {self.email})"


class ContactMaster:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        print(f"Added contact: {new_contact}")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        print(f"Deleted contact with name: {name}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Found contact: {contact}")
                return contact
        print(f"No contact found with name: {name}")
        return None

    def display_contacts(self):
        print("Contact List:")
        for contact in self.contacts:
            print(contact)


# Example usage
contact_master = ContactMaster()

# Add contacts
contact_master.add_contact("Alice", "123-456-7890", "alice@example.com")
contact_master.add_contact("Bob", "098-765-4321", "bob@example.com")

# Display all contacts
contact_master.display_contacts()

# Search for a contact
contact_master.search_contact("Alice")

# Delete a contact
contact_master.delete_contact("Bob")

# Display all contacts again
contact_master.display_contacts()
