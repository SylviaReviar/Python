"""
    Okay, so the assignment this time says to calculate interest.
    I was looking at def functions before, and ChatGPT mentioned the return function.
    Since I haven't reached that point yet, I ignored it and focused on just defining new functions first.
    In this way, I think I understand now what it means to create a new command.

    The objective says, "write a Python function named calculate_interest that computes and returns simple interest based on given parameters"
    In other words, it's time to go into debt. Lovely.

    Simple Interest = P * r * t / 100

    Here are the variables I'll be using:
    simple_interest = principal * interest_rate * time / 100

    And then I have to use the return keyword to send back the computed interest to a variable in main...
    Then print the result. Oh boy...
    """

# I'm not super confident in my coding skills, but let's at least give it a shot.
# Here we go. Start with a greeting. It's only polite.
# Okay so side note: I didn't realize interest could also have to do with investments for some reason?
# So I went with a loan scenario. This means I not only have to calculate interest, but add it on top of the initial loan amount too.
# I'll include that in the assignment just to prove I know what I'm doing.


def greet():
    print("Hello. Today we will be calculating your interest rate.")
    print("I know, I know. It's boring, isn't it?")
    print("Unfortunately, we have to know these things.")
    print("But unfortunately, you did take out that loan a few years ago...")
    print("And my job is to tell you how much you owe now.")
    print("So please bear with me! Let's get through this together.")
    print("Ready? Let's begin.")


def calculate_interest():
    principal = float(input("How much was the initial loan you took?: "))
    interest_rate = float(
        input("And how much was the interest rate at the time you took that loan?: "))
    time = float(
        input("Last question! How long ago did you take this loan in years?: "))
    simple_interest = principal * interest_rate * time
    total_owed = simple_interest + principal
    return simple_interest, total_owed


def main():
    greet()
    interest, owed = calculate_interest()

    print("Thank you for your patience!")
    print(f"The interest you owe is {interest:,.2f}.")
    print(f"However, the total you must pay back amounts to {owed:,.2f}.")
    print(f"If you'd like to set up a payment plan, please contact (XXX) XXX-XXXX.")
    print(f"Thank you for choosing our company!")


main()
