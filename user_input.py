"""
    Using Code to interact with users
    """

first_name = input("What is your first name? ")
print(f"Hello, {first_name}.")
# use int for conversion from strings to integers
age = int(input("How old are you? Please use numerals. "))
# age = int(age)
print("You are " + str(age) + " years old.")
new_age = age + 1
print(f"Next year, you will turn {new_age}.")
# I think this is supposed to be an alternate way to print that, but it's not working??
print("You will turn " + str(new_age) + " next year.")

# Replication operator
print("_" * 50)
