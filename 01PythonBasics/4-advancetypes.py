# List create with text
my_list = ['apple', 'banana', 'cherry']
# List create with numbers
my_numbers = [1, 2, 3, 4, 5]

# print first and last item of the list
print("First item:", my_list[0])
print("Last item:", my_list[-1])
#add an item to the list
my_list.append('mango')
#addd item in middle of the list    
my_list.insert(2, 'orange')
print("Updated list:", my_list)
##extract data from the list    
print("Extracted item:", my_list[1:-1])  # Extract items from index 1 to n-1st value
## count the number of items in the list
print("Number of items in the list:", len(my_list))
##remove an item from the list  
my_list.remove('banana')
# remove the last item from the list        
my_list.pop()
# list membership test
if 'apple' in my_list:
    print("'apple' is in the list")
# List concatenation
new_list = my_list + my_numbers 
print("Concatenated list:", new_list)   
# List Comprehension
squared_numbers = [x**2 for x in my_numbers]
print("Squared numbers:", squared_numbers)

###Example of sets
# Sets are unordered collections of unique elements
# Example of creating a set
my_set = {1, 2, 3, 4, 5}
# Adding elements to a set
my_set.add(6)
# Removing elements from a set
my_set.remove(2)
# Checking membership in a set
if 3 in my_set:
    print("3 is in the set")
# Set operations
union_set = my_set.union({7, 8})
intersection_set = my_set.intersection({3, 4, 5})
# Printing the results
print("Union of sets:", union_set)
# Printing the intersection of sets
print("Intersection of sets:", intersection_set)


##Tuples
# Tuples are immutable sequences
# Example of creating a tuple
my_tuple = (1, 2, 3, 4, 5)
# Accessing elements in a tuple
print("First item in tuple:", my_tuple[0])
print("Last item in tuple:", my_tuple[-1])
# Tuple unpacking
a, b, c, d, e = my_tuple
print("Unpacked values:", a, b, c, d, e)
#mixed data type tuple
mixed_tuple = (1, "hello", 3.14, [1, 2, 3])
print("Mixed tuple:", mixed_tuple)  
#nested data structure in tuple
nested_tuple = (1, 2, (3, 4), [5, 6])
print("Nested tuple:", nested_tuple)

#single element tuple
single_element_tuple = (42,)    
print("Single element tuple:", single_element_tuple)


#Dictionaries
# Dictionaries are collections of key-value pairs
# Example of creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# Accessing values in a dictionary
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])
print("City:", my_dict['city'])
# Adding a new key-value pair to the dictionary
my_dict['job'] = 'Engineer'
# Removing a key-value pair from the dictionary
del my_dict['age']
# Checking if a key exists in the dictionary
if 'name' in my_dict:
    print("Name is in the dictionary")
# Iterating over key-value pairs in the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Dictionary comprehension
squared_dict = {x: x**2 for x in range(1, 6)}
print("Squared dictionary:", squared_dict)


