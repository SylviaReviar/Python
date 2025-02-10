"""
Clothing choice based on temperature
Assuming going to school as the activity
"""

temp = float(input("What is the current temperature in Fahrenheit?: "))
if temp <= 0:
    print("Let's bring a coat, then...")

elif temp < 32:
    print("Brrr... Time for long sleeves.")

elif temp < 50:
    print("Midwest Spring.")

elif temp < 70:
    print("Barbecue grill tonight!")
    print("Camping trip, anyone?")

elif temp < 120:
    print("Summer is here! Time to hit the beach.")

else:
    print("...maybe stay inside. The sun is a deadly laser...")
