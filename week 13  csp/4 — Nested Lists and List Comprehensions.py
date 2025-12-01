# Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.
fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

fruits[0]
print(groceries)
# print(groceries)[0][1]
# print(groceries)[1][2]
# print(groceries)[2][2]

for collection in groceries:
    for food in collection:
        print(food, end=" ") #, end=" "
    # print(collection)
    print()
print("_")
# List comprehensions provide a concise way to create lists.

# Examples:Objective:
# Students will manipulate nested lists and understand basic list comprehensions.

# Key Notes:

# A list can contain other lists.
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))
for row in num_pad:
    for num in row:
        print(num, end=" ") #, end=" "
    print()

# List comprehensions provide a concise way to create lists.

# Examples:

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])    # 6

# List comprehension
first_col = [row[0] for row in matrix]
print(first_col)       # [1, 4, 7]



# Practice Problems:

# Build a matrix variable containing 3 lists of 3 numbers each.
matrix2 = [
    [8, 10, 11],
    [4, 6, 7],
    [1, 81, 90]
]
# Print the first list.
print(matrix2[0])
# Print the second item from the third list.
print(matrix2[2][1])
# Use a list comprehension to extract the last item from each sub-list.
attempt = [row[2] for row in matrix2]
print(attempt)
# Challenge: Create a new list containing squares of numbers from 1–10 using a comprehension.
squares = [x**2 for x in range(1,11)] #for numbers 1-10 it squares them
for x in range(1, 11):
    print(x**2) 
    # Doubles x
# m3 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9, 10]
# ]
# print(m3[2][3])