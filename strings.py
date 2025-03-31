"""
    oh god spring break is over as of tomorrow. Sorry it took me so long to get to this...
    I wore myself down trying to rush on my game development project, beating myself up and drawing
    over and over like my life depended on it
    ended up giving myself HUUUUUGE headaches...
    and i crashed out HARD. even now, I'm fighting through another headache to try and get this done.

    The assignment says to complete the code given to us by Meri.
    Where it says TODO: I have to follow the instructions.

    here goes everything I guess

    ...never mind my brain isn't working. I'm waiting til tomorrow...
    
    3/31/25: Ok I'm back. Let's take a crack at this now...

    Wow that was surprisingly simple and fast. I feel silly for getting a headache over this yesterday...
    """


def main():

    # Example string
    example_string = "Hello, Python programmers!"
    # TODO: Iterate through the string and print each character
    for i in example_string:
        print(f"Iterating through the string: {i}")
    # TODO: Find and print the character with the minimum ASCII value in the string
    print(f"\nCharacter with the minimum ASCII value: {min(example_string)}")
    # TODO: Find and print the character with the maximum ASCII value in the string
    print(f"\nCharacter with the maximum ASCII value: {max(example_string)}")
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print(f"\nIndex of 'o': {example_string.index("o")}")
    # TODO: Convert the string into a list of characters and print the list
    list_of_string = list(example_string)
    print(f"\nConverting string to a list of characters: {list_of_string}")
    # TODO: Count and print the number of occurrences of 'o' in the string
    print(f"\nCount of 'o' in the string: {example_string.count("o")}")


main()
