"""
    Congratulations! You won a free ticket to watch the Fortune Cup in New Domino City's Duel Stadium!
    This is a big moment for you. You finally get to see the King in action!
    All that's left now is to choose your seat, and the seats for your family members!

    In your section, you have the choice of 20 seats numbered 1 to 20.
    We will display the list of available seats for you, and you choose one seat per person.
    (If you enter 0, that will end your selection process, and we will save those seats for you!)
    Once you make your decision, we will remove that seat from the available choices and update the list.
    If you select an invalid or already-sold seat, we will ask you to try again. Don't steal someone else's seat!
    And, of course, have fun. Look forward to seeing the best Turbo Duels of your life!

    ((Just as a note, this is also the instructions given on the assignment. I'm just playing a little pretend!))
    """

# Okay. First, let's create the list. It should have 20 seats numbered 1-20.
fortune_seats = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
taken_seats = []

# I hope that works. Next, let's print them so the customer can see the available seats.

print("Welcome to the Fortune Cup!")
print("If you're reading this, you've won a free ticket, or you are purchasing a new one.")
print("We will display the list of available seats for you. Choose which one you want!")
print("When you're finished choosing, please enter \"0\" to end the selection process.")
print("Now then...")

vacant_seats = len(fortune_seats)

# Okay. Next, I need a way to check for valid inputs...
chosen_seats = 1

while chosen_seats != 0:
    print(f"There are {vacant_seats} seats available.")
    chosen_seats = int(
        input("Please enter which seat you would like. When you're done, press 0: "))
    if chosen_seats > 20 or chosen_seats < 0:
        print(
            "That is not a valid seat number. Please try again. Enter 0 when you're done.")
    taken_seats.append(fortune_seats[chosen_seats - 1])
    fortune_seats.pop(chosen_seats - 1)
    print(f"Currently available seats: {fortune_seats}")
    print(f"Seats you have chosen: {taken_seats}")

# Current errors: Selecting 0 adds Seat 20 to the list of chosen seats.
# Also: I want to add a message when you've pressed 0 that says "Your chosen seats are: {taken_seats}. Thank you and enjoy the Fortune Cup!"
# This will make it better for the user experience, and tie up the program in a neat bow.
# I know I'm supposed to figure this stuff out on my own now, but...
# I'm struggling to grasp the order of logic. It makes sense, but it's still hard.
# This is what I'd like to go over with Meri tomorrow.

# Is it possible to do something like "if chosen_seats = seat in taken_seats:"? There's supposed to be a check as well for taken seats...
# I don't know how I would even go about writing something like that.
# I need help learning how to do this in the first place. Once I've finished learning from the tutoring session, I'll see if I can touch it up a bit.

# I would like the assistance to be listed as such: "Use these functions to make this happen." Having hints like that would be super helpful.
# I was able to figure out how to do it before with those hints. I get that I should be at a point where my hand isn't being held anymore...
# But I'm still struggling to grasp the functions which is why I need it still. I feel inadequate being unable to just "figure it out" on my own.
# Hence why I haven't written any code yet. I don't know where to start. Once I do know, I'd like to try it myself, then ask for help again.
