# Dictionaries are exactly what the word means...a term + definition. AKA key-value pairs.
# Dictionaries are not ordered; they're sorta like a database; each term has to be unique but definitions can be the same (sorta like synonyms in a dictionary); there can also
# be multiple definitions for a single term


gradeDict = {'Kelly':89, 'Adam':91, 'David':65, 'Ashley': 83}

print("The class of 4 students all earned the following scores on the last test:", gradeDict)

print('David received a: ',gradeDict['David'])


# To change a single value in the dictionary, use the code below:
gradeDict['David']=61
print(gradeDict)

# To add an additional single value to the dictionary, use the code below:
gradeDict['Jessy'] = 100

print(gradeDict)

# To remove a single value from the dictionary, use the code below:
del gradeDict['David']
print(gradeDict)

# As in vocabulary dictionaries used for spelling and definitions, python dictionaries can have terms with multiple defintions.
# Using the code below, we can have multiple test scores for each student
gradeDict = {'Kelly':[89,91],
             'Adam':[91,95],
             'Ashley':[83,80],
             'Jessy':[100,100]}
print(gradeDict)

# Print all test scores for a single student
print(gradeDict['Jessy'])

# Print a specific test score for a single student
print(gradeDict['Jessy'][0])