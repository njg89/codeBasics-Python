# Designate a custom syntax for a default function like th example 'statistics.mean()' below:
'''
import statistics as stat
exList = [5,3,2,9,7,4,3,1,8,9,10]

print(stat.mean(exList))
'''

# Only utilize one function, like the 'mean' example below:
'''
from statistics import mean
exList2 = [3,2,3,5,6,1,0,3,8,7]

print(mean(exList2))
'''

# Utilize multiple functions while renaming each
'''
from statistics import mean as m, stdev as std
exList2 = [3,2,3,5,6,1,0,3,8,7]
print('The set is: ', exList2,'\n')

print('The Mean of the set is: ')
print(m(exList2))
print('\nThe Standard Deviation of the set is: ')
print(std(exList2))
'''

# Import statistics with all functions without needing to type out the entire 'statistics.mean' function
'''
from statistics import *
exList2 = [3,2,3,5,6,1,0,3,8,7]
print('The set is: ', exList2,'\n')

print('The Mean of the set is: ')
print(mean(exList2))
print('\nThe Standard Deviation of the set is: ')
print(stdev(exList2))
'''