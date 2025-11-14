# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.
#Lists are part of the collections family in Python
# Creating a list
my_list = [1,2,3,4.5]
print(my_list) # [1, 2, 3, 4, 5]
print(len(my_list)) # 5
print(type(my_list)) # <class 'list'>
print(my_list[0]) # 1
print(my_list[1:4])
print(my_list[1:]) # [2,3,4,5]
print(my_list[:-1]) # [1, 2, 3, 4
#reverse the list
print(my_list[::-1]) # [5, 4, 3, 2, 1]
#Modifying a list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # (1, 2, 3, 4, 5)
#Add 7 and 8 to the end of the list
my_list.extend([7,8])
print(my_list) # [1, 2, 3, 4, 5, 6, 7]
my_list.extend([9,10,11])
print(my_list)
#Remove the last item
my_list.pop()
print(my_list) # [1,2,3,4,5,6,7]
my_list.pop(2)
print(my_list) # [1,2,3,4,5,6,7,
#reverse the list
my_list.reverse()
print(my_list) # [7, 6, 5, 4, 3, 2, 1]
# my_list.remove(4)
# print(my_list) # [7, 6, 5, 2 ,1]
#remove the last item using negatives

#Add 50 more to the end if the lines
new_list = list(range(12,10))
print(new_list)
my_list.append(new_list)
print(my_list)
#my_list.extend(new_list)
#print(new_list)
new_list = list(range(1,100))
print(new_list)

#print every 3rd item in the list
print(my_list[ : : 3])
#Tenth numbers
print(new_list[ : : 10])
#remove every 3rd item in the list
del my_list[ : : 3]
print(len(my_list))
print(my_list)

#list functions
# .append () - adds an item to the end of the list
# .extend() - adds multiple items to the end of the list
# .pop() - removes and returns an item at a given index
#   (default is the last item)
# .remove() - removes the first occurrence of a specific value
# .sort() - sorts the list in ascending order
# .reverse() - reverses the order of the list

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

# collection

# Practice Problems:

# Create a list with 5 of your favorite foods.

# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.