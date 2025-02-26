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
fortune_seats = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
                 "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]

# I hope that works. Next, let's print them so the customer can see the available seats.

print("Welcome to the Fortune Cup!")
print("If you're reading this, you've won a free ticket, or you are purchasing a new one.")
print("We will display the list of available seats for you. Choose which one you want!")
print("When you're finished choosing, please enter \"0\" to end the selection process.")
print("Now then...")

print(f"Seats available: {fortune_seats}")

# Okay. Next, I need a way to check for valid inputs...
chosen_seats = input("Please select the seat you want: ")
