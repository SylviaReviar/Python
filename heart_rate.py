"""
   My heart rate monitor

   Define time_slots as a list with times of day ("Morning", "Midday", "Afternoon", "Evening").
   Use a loop to prompt the user for heart rate (BPM) at each time slot.
   Create a multi-level list heart_rates to store the time lots and their corresponding heart rates.
   Calculate the average heart rate and display it.

   I wish I could make it funnier or cuter, but for now, let's just do what we were told...
   """

# First, let's add the times.
heart_rate_times = ["morning", "midday", "afternoon", "evening"]
total = 0

heart_rate_with_times = []
confirmed_number = "N"

# Now, user input.
for time in heart_rate_times:
    if confirmed_number == "N":
        heart_rate = int(
            input(f"Please enter your heart rate in BPM this {time}: "))
    while (heart_rate > 200 or heart_rate < 45) and confirmed_number == "N":
        confirmed_number = input(
            f"{heart_rate} BPM is outside the normal range. Are you sure? (Y or N): ")
        if confirmed_number == "Y" or confirmed_number == "y" or confirmed_number == "Yes" or confirmed_number == "YES" or confirmed_number == "yes":
            print("Please call emergency services. I'm worried about you.")
            break
        else:
            heart_rate = int(
                input(f"Please enter your heart rate in BPM this {time}: "))
    heart_rate_with_times.append([time, heart_rate])
print(heart_rate_with_times)

# Show the user the results

if confirmed_number == "N":
    for item in range(len(heart_rate_with_times)):
        print(
            f"This {heart_rate_with_times[item][0]}, your heart rate was {heart_rate_with_times[item][1]}")
    # Now to calculate the average...
        total += heart_rate_with_times[item][1]
    average = total / len(heart_rate_with_times)
    print(f"Your average heart rate today was: {average:.1f}")
