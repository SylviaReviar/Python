"""
    Sonya Rozenfeld

    Using "and," "or," and "not" operators. The goal is to:
        - Use user input to assign to a variable.
        - Determine how the variable compares to other variables.
        - Use boolean values to indicate results.

    """

# Instructions from Assignment on Canvas:

# 1. Ask user to input two integers.

x = int(input("Please enter a whole number to assign to x: "))
y = int(input("Please enter a whole number to assign to y: "))

a = 10
b = 50
c = 100

# 2. Implement six logical comparisons, using two of each: "and," "or," and "not".
# I think I get what I need to do from here. Walking it through with notes helps!
# P.S. I added an extra variable (c) to ensure I was understanding things correctly,
# and not just copying my notes mindlessly.

# I have encountered a slight problem. I may not understand the "and" comparison.
# If I input one of the variables to be less than a (10), but the other variable is bigger...
# Then for some reason, it seems to believe that both are greater? Or at least, that's what it prints.

# I realized why. I did "if x and y > a", so it only checked for y's comparison.
# I wonder if it's possible to shorthand it by using parentheses? I'll ask later in class.

# This is "and".

if x > a and y > a:
    print(f"\nBoth x ({x}) and y ({y}) are greater than a ({a}).")
else:
    print(f"\nX ({x}) and y ({y}) are not both greater than a ({a}).")

if x < b and y < b:
    print(f"Both x ({x}) and y ({y}) are less than b ({b}).")
else:
    print(f"X ({x}) and y ({y}) are not both less than b ({b}).")

if x < c and y < c:
    print(f"Both x ({x}) and y ({y}) are less than c ({c}).")
else:
    print(f"X ({x}) and y ({y}) are not both less than c ({c}).")

# This is "or".

if x < a or y < a:
    print(f"\nEither x ({x}) or y ({y}) is less than a ({a}).")
else:
    print(f"\nNeither x ({x}) nor y ({y}) is less than a ({a}).")

if x < b or y < b:
    print(f"Either x ({x}) or y ({y}) is less than b({b}).")
else:
    print(f"Neither x ({x}) nor y ({y}) is less than b({b}).")

if x < c or y < c:
    print(f"Either x ({x}) or y ({y}) is less than c ({c}).")
else:
    print(f"Neither x ({x}) nor y ({y}) is less than c ({c}).")

# This is "not".

if not x > y:
    print(f"\nX ({x}) is less than y ({y}).")
else:
    print(f"\nY ({y}) is less than x ({x}).")

if not x < c:
    print(f"X ({x}) is greater than c ({c}).")
else:
    print(f"C ({c}) is greater than x ({x}).")

if not y > a:
    print(f"A ({a}) is greater than y ({y}).")
else:
    print(f"Y ({y}) is greater than a ({a}).")
