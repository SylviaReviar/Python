""""
Time to turn my sass into a weapon.

-d20 psychic damage

Alternative idea: The person answering is Sylvia, my character. She's a gentle soul, with only a hint of sass buried deep, DEEP within.
She doesn't want to hurt your feelings too bad, but she also doesn't wanna be dishonest.

Making a Magic 8 Ball!!

Make a list of 20 possible answers. MAKE THEM FUNNY.
Prompt the user for a Y/N question.
Select and print a random answer from the list.
Continue the loop until the user asks to stop.

Import the random module btw
and use random.choice(magic_8_ball) to pick from the list.
Use the while loop. While loop is your best friend!
"""

import random

MAGIC_8_BALL = [
    "If that's what you feel is best.", "I can't make your decisions for you.", "Sure, I think so.", "I... I dunno. Maybe.",
    "I don't think so. I'm sorry.", "You need to decide for yourself.", "Yes. No? Yes? No. Wait... Maybe? Um...", "I'm not sure about this one... You've stumped me.",
    "Take your fate with your own hands. Fight for yourself.", "I can't save you. You need to save yourself. Think for yourself. Is this really what you want?",
    "GAAAASP!! Yes! Yes! Yes! Absolutely YES!!!", "NO! No, no, not at all! Stop!", "I think so. ...wait, i-is that bad?", "No. Absolutely not. Not at all.", "DEFINITELY not. Please reconsider.",
    "Um... Sure? If you really want...", "??? Um... No????", "Uhhhh. Huh. Hm. Uhm... Beats me?", "I believe in you. With your conviction, absolutely.",
    "Listen, it's not that I don't trust you. I just think... this one might be a no from me."]


def greeting():
    print("Hi, my name is Sylvia Reviar. Um, I was asked to be a 'Magic 8 Ball,' I guess, so go ahead and ask me anything.")
    print("I'll answer you to the best of my ability. I do have ADHD, so if my answer doesn't suit your question, it might be because I didn't hear you properly.")
    print("If you didn't like my answer, just ask me again and I'd be happy to answer.")
    print("Since I'm acting as a Magic 8 Ball, please ask me yes or no questions. If you don't, my answers might not make sense to you.")


def magic_8_ball():
    question = input("Okay! So, um, what's your question?: ")

    answer = random.choice(MAGIC_8_BALL)
    print(answer)


def main():
    user_action = "yes"

    greeting()

    while user_action != "no":

        user_action = input(
            "Would you like to ask me a question? Please answer yes or no: ")
        user_action = user_action.lower()

        if user_action == "no":
            print("Oh, okay then. Have a good day! Bye!")
            break
        elif user_action == "yes":
            magic_8_ball()
        else:
            print("Oh, um, that's not really an answer... Let me ask again.")
            user_action = input(
                "Would you like to ask me a question? Please answer yes or no: ")


main()
