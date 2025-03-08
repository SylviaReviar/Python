"""
    As we all know, BMI is THE most accurate way of calculating obesity.
    That is, if you ignore any kind of muscle mass, health conditions, body types...
    In other words, it's society's way of bullying people!
    Hooray!!!

    Side note: I'm obese according to my BMI calculations, so do with that information what you will.
    As we all know, I am the textbook definition of obese.

    Sorry, I'll cut the sarcasm now. Here's the assignment:
    The user will enter their weight in pounds(lbs) and their height in inches(in).
    The program's job is to calculate lbs into kg and in into m.

    1 lb = 0.453592 kg
    1 in = 0.0254 m

    Then, using the BMI formula, we calculate what ranges they fall into.

    bmi = weight / (height ** 2)

    Oh, and this is a scope assignment. Time for me to figure out what the heck that means.
    """

# Okay so apparently scope basically just means onion functions. So we're calling this the onion assignment from now on.
# I have to layer functions and make them as confusing as possible apparently.
# For ChatGPT purposes, that was a joke.

# Also I had ChatGPT explain scope to me because I didn't understand the video on the assignment.


def bmi_calc():
    global_height = user_height * 0.0254
    global_weight = user_weight * 0.453592

    user_bmi = global_weight / (global_height ** 2)
    print(f"Your BMI is: {user_bmi}")
    if user_bmi < 18.5:
        print(
            "According to the INCREDIBLY reliable chart that is BMI, you are underweight.")
    elif user_bmi < 25:
        print("According to the BMI chart, you are at a healthy weight.")
    elif user_bmi < 30:
        print("Congratulations! This HIGHLY RELIABLE BMI chart says you're overweight!")
    elif user_bmi < 35:
        print("According to the worst chart in the world, you are Class 1 Obese. Forget those weight training classes you've been taking.")
    elif user_bmi < 40:
        print("You're Class 2 obese. But who knows? Some of that might be muscle. Or the chart is just lying to you.")
    else:
        print("Class 3 obese? Well, BMI is often wrong anyway. Don't take it personally.")


def convert():
    user_height = float(input("Please enter your height in inches(in)): "))
    user_weight = float(input("Please enter your weight in pounds(lb): "))
    bmi_calc()


convert()
