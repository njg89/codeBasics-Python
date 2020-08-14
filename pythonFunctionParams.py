#simple calculator
print("---SIMPLE CALCULATOR:ADDITION ONLY---")
def addition (num1,num2,num3,num4):
    answer = num1+num2+num3+num4
    return answer

x = addition(5,6,4,10)
print(x,'\n')

#basic website function with very very basic parameters
print("---BASIC WEBSITE---\n")
def website(font='TNR',
            background_color='white',
            font_size='11',
            font_color='black'):

    print('font:',font)
    print('bg:',background_color)
    print('font size:',font_size)
    print('font color:',font_color)

'''to change the default value of a function parameter, include the parameter name when the function is being called, like the example below:
website(background_color='white'
'''
website(font_size='22')

'''If the code below were to be used, we would have to define every parameter every time vs. the default params being set as seen in lines 12-15.
website('TNR','white','11','black')
website(font='TNR',
        background_color='white',
        font_size='11',
        font_color='black')
'''