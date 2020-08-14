#a lot of python practitioners do not condone global variables
x = 6

print("--BEGIN EXAMPLE FUNCTION--")
def example():
    print(x)

example()

#example2() considered best practice for assigning variables and returning it to a global variable
print("---BEGIN EXAMPLE2 FUNCTION---")
def example2():
    z = 7
    print(z)
    y = x + 1
    print(y)
    return(y)

x = example2()
print(x)

#the code below is considered NOT best practice
print("---BEGIN EXAMPLE3 FUNCTION")
def example3():
    global x
    x += 1
    print(x)

example3()