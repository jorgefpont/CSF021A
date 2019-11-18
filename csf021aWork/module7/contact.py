"""
Defines class Contact
"""
class Contact:
    """
    One object of class Contact represents one person's contact info.
    """
    def __init__(self, name, phone, email, streetAddress):
        """"
        initializes every new object of class Contact
        """
        self.name = name
        self.phone = phone
        self.email = email
        self.streetAddress = streetAddress

    def __str__(self):
        """
        returns a string containing the data in the Contact
        """
        return "%s\n%s\n%s\n%s\n" % (self.name,
                                     self.phone,
                                     self.email,
                                     self.streetAddress)

# Tests class Contact
if __name__ == "__main__":
    friend1 = Contact("Mickey", "650-345-3333", "Mickey@disneyland.com", "disneyland, CA")
    print (friend1)