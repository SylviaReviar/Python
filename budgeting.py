"""
    Requirements:  
    Housing (rent or mortgage)
    Utilities
    Groceries
    Transportation
    Health Care
    Personal Care
    Clothing
    Debt
    """

# HOUSING CALCULATIONS

# Let's interact with the user

budget = float(input("Please enter your monthly income for the budget: "))
housing = float(input(
    "Please enter your housing costs (rent or mortgage costs plus HOA if you have it): "))

# Let's set up the calculations...
housing_percent = housing/budget * 100

# And now for the output!
print(f"Your housing is {housing_percent:.1f}% of your monthly budget.")

# Let's add more variables.

utilities = float(input("Please enter the cost of utilities: "))
groceries = float(input("Please enter the cost of groceries: "))
transportation = float(input("Please enter the cost of transportation: "))
health_care = float(input("Please enter the cost of healthcare: "))
personal_care = float(input("Please enter the cost of personal care: "))
clothing = float(input("Please enter the cost of clothing: "))
debt = float(input("Please enter the cost of debt: "))

# CALCULATIONS

utility_percent = utilities/budget * 100
groceries_percent = groceries/budget * 100
trans_percent = transportation/budget * 100
health_percent = health_care/budget * 100
personal_percent = personal_care/budget * 100
clothing_percent = clothing/budget * 100
debt_percent = debt/budget * 100

# OUTPUTS

print(f"Your utilities are {utility_percent:.1f}% of your budget.")
print(f"Your groceries are {groceries_percent:.1f}% of your budget.")
print(f"Your transportation is {trans_percent:.1f}% of your budget.")
print(f"Your healthcare is {health_percent:.1f}% of your budget.")
print(f"Your clothing is {clothing_percent:.1f}% of your budget.")
print(f"Your debt is {debt_percent:.1f}% of your budget.")
