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
# Why is a list more useful than a variable
#A list can hpld multiple values.
# While a variable can only hold one value at a time
cakes = ['chocolate', 'vanilla', 'red velvet', 'carrot']
print(cakes)
#access the first item
print(cakes[0]) # chocolate
# access the last item
print(cakes[-1]) # carrot
#want to chocolate cake instead of vanilla
cakes[0] = 'strawberry'
print(cakes)
cakes.append('lemon')
print(cakes)
cakes[1] = 'chocolate'
print(cakes)
#Remove the last cake
cakes.pop()
print(cakes)
#Insert a new cake at index 2
cakes.insert(2, 'funfetti')
print(cakes) # ['strawberry', 'chocolate', 'funfetti']

# Examples:

my_list = ['apple', 'banana', 'cherry']
# print(my_list[0])         # apple
# print(my_list[1:])        # ['banana', 'cherry']

# my_list.append('grape')
# print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)

# collection

# Practice Problems:

# Create a list with 5 of your favorite foods.
e_list = ['potatoes', 'pizza', 'beans', 'fries', 'chicken']
print(e_list)
# Print the second and last item.
print(e_list[-1])
# Add a new item using .append().
e_list.append('jelly')
print(e_list)
# Remove the first item using .pop(0).
e_list.pop(0)
print(e_list)
# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.

#Sets = [1, 2, 3]
#Sets are unordered collections of unique items
#Sets do not support indexing or slicing
#Sets are mutable
#Sets are created using curly braces
#Do sets allow duplicate items? No, sets do not allow duplicate items
my_set = {1, 2, 3, 4, 5}
print(my_set) # (1, 2, 3, 4, 5)
print(type(my_set)) # <class 'set'>
#add an item to the set
my_set.add(5)
#check if an item is in the set
print(4 in my_set) # True
print(3 in my_set) # False

# Tuples are an ordered collections of items
# Tuplesm are an immutable. meaning you cannot modify them after creation
# Tuples are created using  parentheses ()
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(type(my_tuple)) # <class 'tuple'>
print(my_tuple[0]) # 1
print(my_tuple[1:4]) # [2, 3, 4]
#Try to modify the tuple (Will raise an error)