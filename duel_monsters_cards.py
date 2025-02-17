"""
    Write the program "99 Bottles of Beer on the Wall" using a while loop.
    Be mindful to change the word 'bottles' to 'bottle' when down to the last one.
    You must do the full 99 bottles; the sample shows the last 3 verses.

    I want to change it from bottles of beer to Yu-Gi-Oh! because it's funny.
    Yu-Gi-Oh! is also known as Duel Monsters in the anime, and this song was parodied in a Yu-Gi-Oh! parody.
    The idea is the same, though.
    """

cards = 99
while cards > 1:
    print(f"\n{cards} Duel Monsters cards on the wall,\n{cards} Duel Monsters cards!")
    cards -= 1
    print(
        f"Take one down, trade it around,\n{cards} Duel Monsters cards on the wall!")
    if cards == 2:
        print(
            f"\n{cards} Duel Monsters cards on the wall,\n{cards} Duel Monsters cards!")
        cards -= 1
        print(
            f"Take one down, trade it around,\nOnly {cards} Duel Monsters card on the wall!")
    if cards == 1:
        print(
            f"\nOnly {cards} Duel Monsters card on the wall,\nOnly {cards} Duel Monsters cards!")
        cards -= 1
        print(
            f"Take one down, trade it around,\nNow there's no Duel Monsters cards on the wall!")
        break

# I want to stop the loop after it hits 0, but interrupt it so that instead of printing out...
# "0 Duel Monsters cards on the wall!"
# It'll say...
# "Now there's no Duel Monsters cards on the wall!"
# But it prints out "0 Duel Monsters cards on the wall!" and the beginning verse of the song again...

# I want to change "cards" to "card" at the end as well.
