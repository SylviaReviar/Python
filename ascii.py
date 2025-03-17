"""
    St. Patty's Day Notes

    Meri says we need to do this.

    Also: 

    Start Your Python Script:
        Open your Python environment and start a new script.
        Use a main() function to organize your code.

        Prompt for User Input:
        Ask the user to enter a single character using input().
        Validate the Input:

    Ensure the user enters precisely one character.
    Use len() to check input length.

    Convert to ASCII Value:
        Use the built-in function ord() to get the ASCII value.
            Example:
            ascii_value = ord(user_input)
            Display the Result:
            Print the ASCII value to the user.

    Reverse Lookup:
        Prompt the user to enter an ASCII value.
        Ensure that the value is between 32 and 127.
        Use a try-except block to handle invalid inputs.
        Use the built-in function chr() to get the corresponding character.
            Example:
            character = chr(ascii_input)
    """


def user_menu():
    print("Hi! Welcome to the ASCII converter!")
    print("Which would you like to do?")
    print("   1. Convert from ASCII to a character")
    print("   2. Convert from a character to ASCII")
    print("   3. Quit")

    choice = int(input("\nPlease enter a number from 1 to 3: "))

    return choice


def from_ascii():
    # Get and validate number between 32 and 127
    # Try and except function
    ascii_value = 1
    while ascii_value < 32 or ascii_value > 127:
        try:
            ascii_value = int(input("Please enter your ASCII value: "))
        except ValueError:
            print("That's not a valid ASCII value. Please try again.\n")
        if ascii_value < 32 or ascii_value > 127:
            print("That's out of ASCII range.")

    # Convert FROM ASCII and print
    character = chr(ascii_value)
    print(
        f"\nThe character represented by the ASCII value {ascii_value} is {character}.\n\n")


def to_ascii():
    # Get and validate a single character from user
    # While statement - check length
    length = 2
    while length != 1:
        character = input("Please enter a single character: ")
        length = len(character)
        if length == 0 or length > 1:
            print("Please try again. Make sure you only enter a SINGLE character.")

    # Convert to ASCII and print
    ascii_value = ord(character)
    print(f"\nThe ASCII value of {character} is {ascii_value}.\n\n")


def main():
    choice = user_menu()

    while True:
        if choice == 1:
            from_ascii()
            choice = user_menu()
        elif choice == 2:
            to_ascii()
            choice = user_menu()
        elif choice == 3:
            print("\nOk! See you next time!")
            break
        else:
            print("\nOops! That's not a valid answer. Please try again.")
            choice = user_menu()


main()
