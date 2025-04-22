"""
Hangman Start - Week 10 Strings Demo

This program begins a simple version of Hangman. You will finish it by:
- Adding a list to keep track of guessed letters
- Checking if the letter was already guessed BEFORE checking if it is in the word
- Changing the word list to 15 words on a subject of your choice
- Display how many incorrect guesses they have left 

Starting from here are notes from Sonya:
I think I'll choose Dragon Quest as my theme this time. Basically just, a very standard fantasy JRPG.

Also, not that I'm complaining given how far behind I am, but I'm worried...
This code is nearly complete. It almost feels like I'm cheating :(
Someday maybe I'll try to do a deeper dive into this assignment...
"""

import random

WORD_LIST = ("LUMINARY", "YGGDRASIL", "COBBLESTONE", "QUEEN", "JESTER", "KINGDOM", "TREASURE",
             "MONSTER", "WARRIOR", "SAGE", "SORCERER", "KING", "TOURNAMENT", "THIEF", "PRINCESS")


def game(answer, display):
    wrong = 0
    right = 0
    remaining = 5

    print("Welcome to Hangman!")
    print("Pretty standard; guess the letters until you get the word.")
    print("If you have 5 wrong guesses you will lose!")

    guessed_letters = []

    while True:
        for item in display:
            print(item, end=" ")

        print("\n\n")
        guess = input("Please enter a letter: ").upper()

        # Check if already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        else:
            guessed_letters.append(guess)

        bad_guess = True
        for i in range(len(answer)):
            if guess == answer[i]:
                display[i] = guess
                right += 1
                bad_guess = False

        if bad_guess:
            print("Wrong!")
            wrong += 1
            remaining -= 1
            print(f"You have {remaining} wrong guesses left.")
            if wrong > 5:
                print("You Lose!")
                print("The correct word was:", answer)
                break

        if right == len(answer):
            print("You Win!")
            print("The word was:", answer)
            break


def main():
    answer = random.choice(WORD_LIST)
    display = ["_"] * len(answer)
    game(answer, display)


main()
