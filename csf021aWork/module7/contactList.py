"""
Defines class ContactList, in file contactList.py
"""
import contact
class ContactList:
    """
    One object of class ContactList represents a list of Contact objects. It
    can function as an address book
    """
    def __init__(self):
        """
        initializes a new ContactList object
        """
        self.list = []

    def add(self, newContact):
        """
        adds newContact to the ContactList
        """
        self.list.append(newContact)

    def __str__(self):
        """
        returns a string containing all the data in the ContactList
        """
        returnedString = ""
        for contact in self.list:
            returnedString = returnedString + "\n" + str(contact)
        return returnedString

# tests class ContactList

if __name__ == "__main__":
    myFriends = ContactList()
    friend1 = contact.Contact("Mickey", "650-345-3333", "Mickey@disneyland.com", "Disneyland, California")
    friend2 = contact.Contact("Minnie", "650-345-3344", "Minnie@disneyworld.com", "Disneyworld, Florida")
    friend3 = contact.Contact("Donald", "650-345-3333", "Donald@EuroDisney.com", "EuroDisney, France")
    myFriends.add(friend1)
    myFriends.add(friend2)
    myFriends.add(friend3)
    print (myFriends)