"""
    Did you know my dad is a pilot? He not only loves computers, but he has an airplane of his own and flies as a hobby.
    It's a pretty expensive hobby. But he did recently fly me to a college in that plane of his, so we could check it out and figure out where I'm gonna go from here.

    Anyway, all that is to say, this is why this program is called airplane_speak.

    Onward to victory!

    The assignment says I must:
        - Construct a NATO dictionary called nato_alphabet.
        - Write a function to prompt a user for a word, then change each letter progressively to the NATO alphabet.
        - Use main() for organization?
        - And, naturally, test the program to ensure it works.
    """


def main():
    nato_alphabet = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliette",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-Ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }

    message = input(
        "This is your pilot speaking! Please leave your one-worded message here and I will translate it for you into the NATO alphabet: ")
    message = message.upper()
    for letter in message:
        print(nato_alphabet[letter])


main()
