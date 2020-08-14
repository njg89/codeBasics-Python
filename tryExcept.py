# Basic examples of Try and Accept error handling

# The Try section is the portion of code being 'tested' and will produce exceptions when they occur
try:
    print('Running the code in the try...')
    print('5' + test)


# The exceptions below are what is sent to the user at the console when an error occurs
# For PYTHON27, except Exception, e is the syntax
except Exception as e:
    print('General Exception triggered!')
    print(str(e))

except TypeError as t:
    print('TypeError triggered!')
    print(str(t))

except NameError as n:
    print('NameError triggered!')
    print(str(n))

print('Code continues onward...')