# Prog05: Print the quotient of the two numbers with the decimal point
num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
if num2 != 0:
    print(f'The quotient is: {num1 / num2}')
else:
    print('Cannot divide by zero')
