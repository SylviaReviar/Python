"""
    Grading scale:
    A = 90-100
    B = 80-89
    C = 70-79
    D = 60-69
    F = 59 or below
    """

# First, check the grade a student got on their test.
score = float(
    input("What was the numerical score you got on your most recent test?: "))

if score >= 100:
    grade = str("A+")

elif score >= 90:
    grade = str("A")

elif score >= 80:
    grade = str("B")

elif score >= 70:
    grade = str("C")

elif score >= 60:
    grade = str("D")

else:
    grade = str("F")

print(f"You got a {grade} on your most recent test.")
