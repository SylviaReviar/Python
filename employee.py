"""
    Okay first thing's first: I used sample code from my professor and rewrote it to match the assignment.

    First, I must make an Employee SuperClass.
    Then, a ProductionWorker subclass.

    Employee must have:
    Name
    Number

    ProductionWorker must have:
    Shift number (1 for day, 2 for night)
    Hourly Pay Rate

    The user must be prompted to input the information and display it in the proper categories.
    """

# Creating and using an Employee SuperClass
# and a ProductionWorker subclass
# along with instantiating (making objects)


class Employee:
    # Dog is a Superclass of the HerdingDog class
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_name(self):
        return f"{self.name}"

    def get_number(self):
        return f"{self.number}"

    def set_name(self, name):
        self.name = name

    def set_number(self, number):
        self.number = number

    def __str__(self):
        return f"Employee name: {self.name} \nEmployee number: {self.number}"


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay):
        super().__init__(name, number)
        self.name = name
        self.number = number
        self.shift_number = shift_number
        self.hourly_pay = hourly_pay

    def __str__(self):
        return super().__str__() + f"Shift Number: {self.shift_number} \nHourly Pay: {self.hourly_pay}"

    def get_shift(self):
        if self.shift_number == 1:
            return "Day"
        elif self.shift_number == 2:
            return "Night"
        else:
            print("That is not a valid answer. Please try again.")

    def get_pay(self):
        return self.hourly_pay

    def set_shift(self, shift_number):
        self.shift_number = shift_number

    def set_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay


def main():

    print("\n\n")
    employee1 = Employee("Ralph", "47")
    print("Employee 1: \n")
    employee1.set_name(input("What is this employee's name?: "))
    employee1.set_number(input("What is this employee's number?: "))
    print(employee1)

    print("\n\n")
    pw1 = ProductionWorker("Fiona", "272", 1, 12.5)
    print("Production Worker 1: \n")
    pw1.set_name(input("What is this employee's name?: "))
    pw1.set_number(input("What is this employee's number?: "))
    pw1.set_shift(
        input("What shift does this employee work? (1 for Day, 2 for Night): "))
    pw1.set_pay(input("How much is this employee paid per hour?: "))
    print("\n\n")

    print("\n\n")
    pw2 = ProductionWorker("Luna", "321", 2, 13.0)
    print("Production Worker 2: \n")
    pw1.set_name(input("What is this employee's name?: "))
    pw1.set_number(input("What is this employee's number?: "))
    pw1.set_shift(
        input("What shift does this employee work? (1 for Day, 2 for Night): "))
    pw1.set_pay(input("How much is this employee paid per hour?: "))
    print("\n\n")


main()
