# Lists are mutable (can be changed)
# Tuples are immutable (can't be changed)

print('---BEGIN TUPLES EXAMPLES---')

def example():
    return 15,19

a,b = example()

print(a)
print(b)


print('\n---BEGIN PYTHON LIST EXAMPLES---')
# Remember, lists are ordered

x = [3,2,9,3,5,8,0,1,10,100]

print('The List:', x)

print('Select a single item from the list:', x[5])

# To include new data in a list, name the list 'x' and include .append(data you want to append)
x.append(12)
print('The new list, with 12 appended is now:', x)

# To insert a value into a specific location in the list, use the code below:
x.insert(5,7)
print('The number 7 has now been inserted into the 5th location of the list.', x)

# Remove a single instance of a value in the list
x.remove(8)
print('The number 8 has now been removed from the list.')

# Find out how many instances of a value are in the list:
print('The total number of 3s are:', x.count(3))

# Print the value of an index position
# Remember, list positions begin with 0 NOT 1
print('Find the index position aka position in the list, of the number 12:', x.index(12))