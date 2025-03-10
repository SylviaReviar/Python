"""
    Time to learn how to organize our functions.
    This assignment says to create a function that can calculate factorials.

    First, we take an integer from our user. We'll calculate the factorial for that number.
    In the factorial function, which I believe should be the main(?) function?? we will have to define the base for n first: 0 or 1.
    For the recursive step, the assignment says... to return n * factorial(n - 1) if n > 1.
    And then we prompt the user for a non-negative integer (again???) and call the factorial function.

    I'm gonna be honest, I don't understand any of this... I don't feel confident in my ability to code this.
    My brain is fried chicken. I woke up at 5:30 today and wasted my time like an idiot because I couldn't fall back asleep.

    Time to break my brain even more.
    """


def factorial(n):
    if n == 0 or n == 1:  # Okay, I think I get it?
        return n
    else:
        return n * factorial(n - 1)

# I don't know how "factorial" is supposed to work here. It looks like a variable to me, and it wasn't assigned anything.
# brain spaghetti
# im in spain without the s
# or spain without the a. I can't tell.
# wheeeeeeee

# ...I think I'm a little loopy. Oh dear.


def main():
    n = int(input("Please enter a non-negative integer to find its factorial: "))
    answer = factorial(n)
    print(f"The factorial of {n} is {answer}.")


main()

# Um. It works??? I don't understand how it works, and how it goes back and forth.
# I went into debugging mode. It looks like it takes the n taken by the user, and moves to else (I used a number greater than 1).
# It moves to else, then else calls factorial over and over again until the number is equal to 1.
# Then after that, when it reaches 1, it goes to "return n" and then multiplies???
# That's the step I don't really get. After that, it multiplies as many times as it was subtracted, jumps to main, and gets printed.
# Maybe it's because it returns n, but when it goes to main, n gets called BACK into factorial??
# My brain might start steaming if I try thinking about this any harder. Let's just move on...
