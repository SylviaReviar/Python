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

your_meow_meows = [meow_meow.lower() for meow_meow in your_meow_meows]

swapped = True
while swapped:
    swapped = False
    for i in range(len(your_meow_meows) - 1):
        if your_meow_meows[i] > your_meow_meows[i + 1]:
            your_meow_meows[i], your_meow_meows[i +
                                                1] = your_meow_meows[i + 1], your_meow_meows[i]
            swapped = True
print(your_meow_meows)

# She says this should sort it, but I just copied down what was written on the assignment...
# Let's try to parse this before I pretend I understand the homework and turn it in.
# Why swap? What does that do? It seems like the word "swapped" is treated as a variable.
# Why is it true? And why make it false after making it true?

# Let me go home and figure this out.

# According to the exercise we did in class, the idea of bubble sorting is to swap in order constantly until they're in the right order.
# So... unit[i] > unit[i + 1] must be a check to compare the two and figure out where they go.
# But what is it checking for? I don't think I set a standard of what to check for.
# Is the default for Python sorting strings to be in alphabetical order?

# Let's try running it and analyze how it prints.
# Okay, there's an error when I try to lowercase the names...
# Found the problem: I used the wrong variable. Let's try again.

# Oh! It lowercased all their names, and ordered them... wait. That's weird.
# The order is ['jack', 'crow', 'akiza', 'luna', 'yusei']. That's not alphabetical.

# I don't understand why it ordered them like that. If it was based on the number of letters in their name, Akiza should've been at the end with Yusei.
# If it was in alphabetical order, it should've gone "Akiza," "Crow," "Jack," "Luna," "Yusei".
# I don't understand Bulbasauring :(
# But I can reverse the list. Let's at least do that much, turn it in, and wait for Meri to address my mistakes ^^;

# WAIT I FORGOT SOMETHING! I added it at the end there: swap = True
# What if that fixes it?! I don't know how, but it might! Let's test it!

# YES!! Okay, that somehow did it. I don't know how, but it did. swap = True must've made it ensure that the actual swap happened,
# so the reorganizing could work properly. Not just confirming it, but like...? ??? idk
# I'll have to ask again next week or over inbox messages...;;;

# anyway, NOW let's reverse it.
your_meow_meows.reverse()
print(your_meow_meows)

# Ayyyy! It worked! I only have a billion questions left over, though... I'll need to analyze the code more thoroughly with help.
