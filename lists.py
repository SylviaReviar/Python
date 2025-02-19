"""
    How to add things to list??

    """

ages = []

# # sort and do calculations
age = 99
# while age != 0:
#     age = int(input(
#         "Please enter the corresponding ages as a whole number between 1 and 120 (Enter 0 when you're done): "))
#     if age < 0 or age > 120:
#         print("That is not a valid age.")
#     if age != 0:
#         ages.append(age)
#     print(f"{ages}" + "\n")

# # Sort ages
# sorted_ages = sorted(ages)  # copies and sorts

# # Copy ages
# copied_ages = ages[:]  # copied_ages = slice(ages) is the same thing

# copied_ages = ages.copy()

# # slice example
# phone = [8, 6, 7, 5, 3, 0, 9]

# jenny = phone[0:3]
# print(f"Sliced: {jenny}")

# if 3 in phone:
#     print(f"3 is in the phone number.")

# if 2 in phone:
#     print(f"2 is in the phone number.")
# else:
#     print(f"2 is not in the phone number.")

# ages.sort()
# print(f"Sorted: {ages}/n")

# ages.reverse()
# print(f"Reversed: {ages}/n")

# total = sum(ages)
# average = total / len(ages)

# print(f"The average age is: {average:.1f}")

# delinquent_accounts = [1056, 2008, 3278, 4189]
# # Find the index of 2008 in the list
# for i in range(len(delinquent_accounts)):
#     if delinquent_accounts[i] == 2008:
#         print("The account number 2008 is in the index," i)

# For loops sample
print("Enter in all ten of the ages as whole numbers between 1 and 120. Start with the first 5.")
for i in range(1, 6):
    age = int(input(
        "Please enter the corresponding ages as a whole number between 1 and 120: "))
    if age < 0 or age > 120:
        print("That is not a valid age.")
    if age != 0:
        ages.append(age)
        print(f"{ages}\n")

# Thiiiiiis isn't working =_=
# I'll have to ask for more advice later...
