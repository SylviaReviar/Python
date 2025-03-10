"""
    This is the first time we've been given a written code to try and enhance.

    The goal is to turn this:

    # Simple Python program to calculate the square of a number
    def square_number():

        number = input("Enter a number to square: ")
        squared_number = int(number) ** 2
        print(f"The square of {number} is {squared_number}.")

    square_number()

    into something that uses "try" and "except".
    """

# Simple Python program to calculate the square of a number # Pasted!!
# Now let's figure this out:


def square_number():
    while True:
        number = int(input("Please enter a whole number to square: "))
        try:
            squared_number = int(number) ** 2
        except TypeError or ValueError:
            # I want to make this loop back. I dunno if I can though?
            print("That's not a valid number. Please try again.")
        else:
            print(f"The square of {number} is {squared_number}.")


square_number()
