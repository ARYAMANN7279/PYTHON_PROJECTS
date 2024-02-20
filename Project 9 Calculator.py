calculator = '''
 _____________________
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''

print(calculator)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2==0:
        return "Error:Can't divide by 0"
    return n1 / n2


def calculate(number1, operator, number2):
    if operator == "+":
        return add(number1, number2)
    elif operator == '-':
        return subtract(number1, number2)
    elif operator == '*':
        return multiply(number1, number2)
    elif operator == '/':
        return divide(number1, number2)
go_on='n'
while go_on!='x':
    if go_on=='n':
        number1 = float(input("Enter your first number: "))
        operator = input("Enter your operator: +, -, *, /: ")
        number2 = float(input("Enter your second number: "))
        result = round(calculate(number1, operator, number2),2)
        print(f"The value of {number1}{operator}{number2} is {result}")
        go_on =input(f"If you wanna continue with {result},type 'y'.If you want a new calculation,type 'n'.If you wanna stop, type x:")
    elif go_on=='y':
        number1 = result
        operator = input("Enter your operator: +, -, *, /: ")
        number2 = float(input("Enter your second number: "))
        result = round(calculate(number1, operator, number2),2)
        print(f"The value of {number1}{operator}{number2} is {result}")
        go_on =input(f"If you wanna continue with {result},type 'y'.If you want a new calculation,type 'n'.If you wanna stop, type x:") 
    elif go_on=='x':
        print("Thanks for using the calculator")
        break