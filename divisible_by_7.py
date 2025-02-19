"""
    Write a Python program to find and print all numbers:
    - Divisible by 7
    - Between 1 and 300

    Use a for loop and modulus (%) operator

    oh god, okay... So for starters, modulus means finding a remainder.

    for loop:
        A control flow statement for iteration, allowing repeated execution of a block of code.

    range():
        A build-in Python function for generating a sequence of numbers.

    break:
        Break the loop.

    continue:
        Skip the rest of the current iteration and move on to the next.
    """

for i in range(1, 301):
    if i % 7 != 0:
        continue
    print(i)

# I... I think that's it?? That was fast. Thank you Meri :D
