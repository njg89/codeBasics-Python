# Input allows users to provide data to your program
# For PYTHON27, rawInput() is used instead of input()

# Input from user:
'''
name = input('What is your name?: ')
print('Hello',name)
'''

import statistics

exList = [5,3,2,9,7,4,3,1,8,9,10]
print('The set of numbers we are using is:', exList)

x = statistics.mean(exList)
print('The mean of the set is:', x)

x = statistics.median(exList)
print('The median of the set is:', x)

x = statistics.mode(exList)
print('The mode of the set is:', x)

x = statistics.stdev(exList)
print('The standard deviation of the set is:', x)

x = statistics.variance(exList)
print('The variance of the set is:', x)

