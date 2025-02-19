"""
    This is my bubble sort assignment.

    I originally wanted to do Pokemon types. But then I realized that'd be too much.
    Not only are there 18 of them, I wanted to make it so you had to write them correctly every time,
    with no repeats. Naturally, that's outside of my field of understanding right now, so I have to be boring.
    But I can still make the prompt funny. Hopefully.

    So we'll do favorite characters instead.
    Store the characters in a list, bubble sort it, and then reverse it.
    """

# Oh, I just realized I'm supposed to prompt the user to input the names. Huh.
# Guess I have to tell them what to do...
# Pokemon types is a no-go. Fictional characters will have to do.

# Don't judge my variable names. Actually do. I did this specially for you :)
your_meow_meows = []

# Okay, what did I do last time... I used a "for" loop, but that was when I already had a list.

for i in range(1, 6):
    meow_meow = str(
        input("\nPlease enter one of your favorite characters' names: "))
    your_meow_meows.append(meow_meow)
    print(f"Your favorite characters: {your_meow_meows}")

# Okay, I have the loop set up, I think?
# Yes, it's tested and it works. I don't know what "i" stands for, but if it works it works.
# Now to Bulbasaur it... (And yes, I'm gonna call bubble sorting Bulbasauring from now on. It's funny.)
# Wait. New error... It's not storing yet. It just loops. So let's back up a step, because I think I jumped ahead.
# Let's try this again...
# Not working...

# Debug mode maybe? Before I try that, maybe let's fix the indentations.
# Okay, that fixed it. So NOW I should Bulbasaur it.

# Oh, and Meri, if you're wondering what a "meow meow" is,
# it's a very cringe Internet term for someone's absolute favorite fictional character that they're VERY NORMAL about.
# VERY normal. SO INCREDIBLY normal.

# Anyway. The assignment says the names should be put into lowercase. Let's try that.

your_meow_meows = [your_meow_meows.lower() for meow_meow in your_meow_meows]

swapped = True
while swapped:
    swapped = False
    for i in range(len(your_meow_meows) - 1):
        if your_meow_meows[i] > your_meow_meows[i + 1]:
            your_meow_meows[i], your_meow_meows[i + 1] = names[i + 1], names[i]
print(your_meow_meows)

# She says this should sort it, but I just copied down what was written on the assignment...
# Let's try to parse this before I pretend I understand the homework and turn it in.
# Why swap? What does that do? It seems like the word "swapped" is treated as a variable.
# Why is it true? And why make it false after making it true?

# Let me go home and figure this out.
