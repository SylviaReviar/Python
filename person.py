"""
Making a person class:

Assignment Steps:

    Class Creation: Design a class named Person with the following data: 
    name, address, age, and phone number.

    Accessor and Mutator Methods: Write get and set methods for each piece of data. 
    These methods allow you to access and change the data safely.

    Creating Instances: Write a program that creates three instances (objects) of the Person class. 
    Use one instance for your made-up information and the other two for imaginary friends or family members.

    Display Data: Print out the information stored in each instance. 
    Ensure the output is formatted and easy to read.

"""


class Person:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def get_info(self):
        return f"{self.__name}, {self.__address}, {self.__age}, {self.__phone_number}."

    def get_name(self):
        return f"{self.__name}"

    def get_address(self):
        return f"{self.__address}"

    def get_age(self):
        return f"{self.__age}"

    def get_phone_number(self):
        return f"{self.__phone_number}"

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number


def main():
    sonya = Person("Sonya", "3 Sweetwater Ct.", 22, "333-456-9012")
    print(sonya.get_info())
    sonya.set_name("Meri")
    print(sonya.get_info())

    sylvia = Person("Sylvia", "42 Domino Lane", 17, "454-2797")
    okita = Person("Okita", "1655 Tops District", 19, "457-8810")

    print(sylvia.get_info())
    print(okita.get_info())


main()
