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

# Let's interact with the user

budget = float(input("Please enter your net monthly income for the budget: "))
housing = float(input(
    "Please enter your housing costs (rent or mortgage costs plus HOA if you have it): "))

# Let's set up the calculations...
housing_percent = housing/budget * 100

# And now for the output!
print(f"Your housing is {housing_percent:.1f}% of your monthly budget.")
