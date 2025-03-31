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

    choice = int(input())

    return choice


def main():

    choice = menu()

    while True:
        if choice == 2:
            print("See you next time!")
            break
        elif choice == 1:
            books = []

            while len(books) < 11:
                books = input("Okay! Please enter a book title: ")

        else:
            print("I'm sorry, that's not a valid answer. Please try again.")
            menu()


main()
