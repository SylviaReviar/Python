"""
    Write the program "99 Bottles of Beer on the Wall" using a while loop.
    Be mindful to change the word 'bottles' to 'bottle' when down to the last one.
    You must do the full 99 bottles; the sample shows the last 3 verses.
    """

beer = 99
while beer < 100:
    print(f"\n{beer} bottles of beer on the wall,\n{beer} bottles of beer!")
    beer -= 1
    print(
        f"Take one down, pass it around,\n{beer} bottles of beer on the wall!")
    if beer == 1:
        print(f"{beer} bottle of beer on the wall!")
    if beer == 0:
        break
    print("Now there's no bottles of beer on the wall!")
