"""
    Sonya Rozenfeld

    This assignment says to create a list, add user input, and make basic calculations.
    The assignment itself says to use steps taken per day, but I hope any user input/unit works?
    So long as the functions are the same, right?

    So let's measure something different, just to challenge ourselves. How about...
    Hours spent playing video games?

    Actually, let's not... Hours are harder to measure than steps. It'd be different if it were minutes,
    but who's actually going to tell me exactly how many minutes they've played games?

    Maybe I'd have to do some extra operations? But that'd be a hassle. Let's just stick with the assignment.
    Too bad I can't put a reference in this one...
    """

# First thing's first... Create the list.

days_of_week = ["Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday", "Saturday"]

# Then it says to initialize an empty list... How would I do that again?

weekly_steps = []

# Okay. That should do it. Next is user input... Using a loop? Oof, okay, let's give this a shot...

for day in days_of_week:
    steps = int(input(f"How many steps did you take on {day}?: "))
    weekly_steps.append(steps)

# ...I don't think that's gonna work -_-;;;
# I need to figure out how--
# Never mind! Thanks to the notes, I think I've got it?
