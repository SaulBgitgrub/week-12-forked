# Objective:
# Apply comparison and logical operators to a real-world problem.

# Scenario:
# Write a program that:

# Asks the user for today’s temperature.

# Prints whether it’s cold, warm, or hot using comparison operators.

# If the temperature is out of range (below -10 or above 110), display “Extreme temperature warning!”

# Starter Code:
tO = int(input("What is the temperature outside: "))
if 80 <= tO <= 110:
    print("It is Hot outside")
elif 50 <= tO < 80:
    print("It is Warm outside")
elif -10 <= tO < 50:
    print("It is Cold outside")
else:
    print("Extreme temperature warning!")