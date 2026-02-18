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
