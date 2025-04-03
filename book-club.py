"""
    Welcome to my book club! And by that, I mean my club consisting of books. I'm the only actual reader. The books are the members, not me.

    ...
    Anyway.

    I'll be using a while loop to input book titles.
    Then the user must put in 10 book titles. Those titles will be stored in a list.
    Each title will be properly capitalized within the list, regardless of how the user writes them.
    Once all the titles are collected, a new, sorted list will be created called sorted_books in alphabetical order.
    A for loop will be used to display each title from the list on a separate line.

    And, of course, all of these should be stored within a main() function.

    This'll be the start of my own little personal library!
    Let's get started...
    """


def menu():

    print("Hi there! Welcome to your library!")
    print("Here, we will store the titles of books you enjoy so you can refer back to them.")
    print("We hold a maximum of 10 books, and we sort them by alphabetical order.")
    print("Would you like to store your books?: ")
    print("   1. Yes")
    print("   2. No")

    try:
        choice = int(input("Please enter 1 or 2: "))
        return choice
    except ValueError:
        print("That's not a valid answer. please try again.")
        menu()


def add_more():

    print("Would you like to add another book?")
    print("  1. Yes")
    print("  2. No")

    more_books = 0

    try:
        while True:
            more_books = int(input("Add another?: "))
            if more_books == 1:
                return more_books
                break
            elif more_books == 2:
                return more_books
                break
            else:
                print("That wasn't on the menu. Please try again.")
    except ValueError:
        print("That's not a valid answer. Please try again.")
        add_more()


def main():

    choice = menu()
    library = []
    more_books = 1

    try:
        while more_books == 1:
            if choice == 2:
                print("See you next time!")
                break
            elif choice == 1:
                print("Let's get started.")

                while len(library) < 11:
                    book = input("Okay! Please enter a book title: ")
                    book = book.lower()
                    book = book.title()
                    library.append(book)
                    library = sorted(library)
                    print(library)
                    more_books = add_more()

                    if more_books == 1:
                        continue
                    elif more_books == 2 or len(library) >= 11:
                        print("Here is your current book club library:")
                        for book in library:
                            print(book)
                        print("Thank you for your service!")
                        print("See you next time!")
                        break
            else:
                print("That wasn't on the menu. Please try again.")
                choice = menu()
    except ValueError:
        print("I'm sorry, that's not a valid answer. Please try again.")
        choice = menu()


main()
