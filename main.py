class AddressBook(object):
    pass

#TODO:
class AddressEntry(object):
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
#ToString Method
    def __repr__(self):
        template = "AddressEntry(first_name='%s', " + \
                    "last_name = '%s', " + \
                    "email = '%s', " + \
                    "age = '%s',) "
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.age}"
        # return first_name
        # return last_name
        # return email
        # return age

#TODO: implement this function

entry1 = AddressEntry




if __name__ == '__main__':
    address_book = AddressBook()

    person1 = AddressEntry("Eric", "Idle", None, "March 29, 1943")

    print(person1)
    print(person1.__repr__())
#mutable

#This is the file I pushed
#Hey, I don't understand blah blah blah'