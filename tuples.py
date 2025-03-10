"""
    Tuples time~

    okay, instructions, here we go
    I'll be using this tuple:
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials", "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    I need to write a program that loops to print each class, use len to print how many classes there are, and of course use a main function.
    This seems easy enough.
    """


def main():
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials",
                           "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")

    print(
        f"There are {len(programming_classes)} total programming classes in this building.")
    print("These classes are:")
    for i in programming_classes:
        print(i)


main()
