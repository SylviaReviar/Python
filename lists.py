"""
    How to add things to list??

    """

# ages = []

# # sort and do calculations
age = 99
while age != 0:
    age = int(input(
        "Please enter the corresponding ages as a whole number between 1 and 120 (Enter 0 when you're done): "))
    if age < 0 or age > 120:
        print("That is not a valid age.")
    if age != 0:
        ages.append(age)
    print(f"{ages}" + "\n")

# Sort ages
sorted_ages = sorted(ages)  # copies and sorts

# Copy ages
copied_ages = ages[:]  # copied_ages = slice(ages) is the same thing

copied_ages = ages.copy()

# slice example
phone = [8, 6, 7, 5, 3, 0, 9]

jenny = phone[0:3]
print(f"Sliced: {jenny}")

ages.sort()
print(f"Sorted: {ages}/n")

ages.reverse()
print(f"Reversed: {ages}/n")

# For loops sample
# print("Enter in all ten of the ages as whole numbers between 1 and 120. Start with the first 5.")
# for i in range(1, 6):
#     age = int(input(
#         "Please enter the corresponding ages as a whole number between 1 and 120: "))
#     if age < 0 or age > 120:
#         print("That is not a valid age.")
#     if age != 0:
#         ages.append(age)
#         print(f"{ages}\n")

# Thiiiiiis isn't working =_=
# I'll have to ask for more advice later...
