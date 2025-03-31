"""
    I am the favorite student lmaooooo

    OKAY next step!
    More Python string methods, featuring more pre-written code by Meri for me to complete~

    Let's get cracking :D

    HOOOOOOLY cannoli that's a lot of code
    oof ok let's do this
    """

# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
# Your code here
mystring1 = string1.capitalize()
print(mystring1)

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
# Your code here
mystring2 = string2.center(10, "~")
print(mystring2)

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
# Your code here
mystring3 = string3.endswith("on")
print(mystring3)

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
# Your code here
mystring4 = string4.find("th")
print(mystring4)

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
# Your code here
mystring5 = string5.isalnum()
print(mystring5)

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
# Your code here
mystring6 = string6.isalpha()
print(mystring6)

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
# Your code here
mystring7 = string7.islower()
print(mystring7)

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespace
string8 = "   "
# Your code here
mystring8 = string8.isspace()
print(mystring8)

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
# Your code here
mystring9 = string9.isupper()
print(mystring9)

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
# Your code here
gimmeanumber = separator.join(iterable1)
print(gimmeanumber)
# I had to pause when I realized this wasn't actually "string 10" and string 10 was after this one...
# So now the variable is salty >:(

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
# Your code here
mystring10 = string10.lower()
print(mystring10)

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  python"
# Your code here
mystring11 = string11.lstrip()
print(mystring11)

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "python  "
# Your code here
mystring12 = string12.rstrip()
print(mystring12)

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
# Your code here
mystring13 = string13.replace("python", "snakes. Ssssss...")
print(mystring13)

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
# Your code here
mystring14 = string14.rfind("n")
print(mystring14)

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
# Your code here
mystring15 = string15.split("-")
print(mystring15)

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
# Your code here
mystring16 = string16.startswith("py")
print(mystring16)

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
# Your code here
mystring17 = string17.strip()
print(mystring17)

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
# Your code here
mystring18 = string18.swapcase()
print(mystring18)

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
# Your code here
mystring19 = string19.title()
print(mystring19)

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
# Your code here
mystring20 = string20.upper()
print(mystring20)
