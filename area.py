"""
    I forgot to do the area of a square and circle functions.
    Whoooops! Time to rectify that.

    First: Define the square and circle functions.
        (Use side for square and radius for circle)
    For the Square Function:
        area = length * width
        Also print the results for the user to see.
    For the Circle Function:
        area = pi * radius ** 2
        pi = 3.14
    And, of course, test the functions. If I could make this funny somehow, I would.
    Unfortunately, the math has to math somehow...

    oh. oh I just realized it specifically needs to use the def keyword.
    I... don't understand the def keyword yet. I need to edit my code.

    Okay, so I have officially decided I'm going to add more def functions here until I get what I'm doing.
    First, I'm going to greet the user and explain to them what we're doing.

    (Oh, also, ChatGPT helped me a little by explaining the process to me.)
    (But Meri knows me well enough by now to know I'd never use ChatGPT to cheat or write my code for me.)
    (I HATE having others put words in my mouth, including AI. I used it for practice, not writing.)
    (You can scan my code for cheating if necessary. I promise you I did no such thing.)
    """


def greet():
    user = input("Hello! What's your name?: ")
    print(f"Hello, {user}. I am a simple calculation program.")
    print("I will calculate the areas of a circle and square with your help.")
    print("All you need to do is tell me what the length and width of the square is, and the radius of the circle.")
    print("Are you ready? Let's begin!")


greet()

# Edit time! Okay, let's actually define things first. Calculating for the square is easy.
# Defining it is what I need to practice.


def square():
    w = float(input("Please enter the width of the square: "))
    l = float(input("Wonderful! Now please enter the length of the square: "))
    area = w * l
    print(
        f"If the width of the square you've generated is {w:.2f}, and the length is {l:.2f}, then the area is {area:.2f}.")


square()


def circle():
    r = float(
        input("Now let's move on to the circle. Please enter the circle's radius: "))
    area = 3.14 * r ** 2
    print(
        f"If the radius of the circle you've generated is {r:.2f}, then the area is {area:.2f}. Thank you for playing!")


circle()

# Let's start with the square.
# I don't think I get the def function...
# As far as I know, def

# My thoughts got cut off because I was switching between ChatGPT and Meri for help. I think I've got it? Let's test it out and see.
# I hope it's okay that I used area as the same variable for both functions...
# I even added a greet function to make sure I knew how it worked. Meri said I should leave the parentheses empty because the variable wasn't defined before the function.
# If I go line by line, then the basic functions are: greet, square, and circle.
# The greet command must follow the steps I listed above: determine the user's name, and print out a message for them.
# The square command must follow the steps I listed above: Define w and l by the user's input, calculate the output, and print the results rounded to two decimal places.
# The circle command does something similar, but it only defines r. If I wrote the code correctly, this is what it should do. Now let's test it.

# Yes! I think it worked! Alright, time to submit this!
