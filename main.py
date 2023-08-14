class AddressBook(object):
    pass


class AddressEntry(object):
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age


entry1 = AddressEntry


def print_address(first_name, last_name, email, age):
    print('================New address Entry================= \n')
    print(f'{first_name} \n')
    print(f'{last_name} \n')
    print(f'{email} \n')
    print(f'{age} \n')

    # return first_name
    # return last_name
    # return email
    # return age


"""
________________________HOME WORK_____________________________________________________________________________________________________________


Create a function that prints out all the information from the class
Create a Function to Print the Instance

You need a function that prints out details of an AddressEntry instance. Then you’ll be able to check whether your initialization worked properly.

To do this, follow the steps:

create a function called print that takes first name, last name, email, age as parameters and then prints them out. This function should be declared IN
the class.

Create 5 address entries
Print the address entries
This needs to happen in the MAIN METHOD
Finish the main function 

"""


def main():
    print_address('Everett', 'Loxley', 'xxxxxxxxx', '9')

    print_address('Chris', 'loxley', 'cloxley4@gmail.com', '42')

    print_address('Wendy', 'Loxley', 'wloxley@gmail.com', '41')

    print_address('Avery', 'Loxley', 'averyloxley@gmail.com', '6')

    print_address('Tyrell', 'baker', 'tybaker1@csumb.edu', 'xx')


if __name__ == '__main__':
    main()

