#calculator
from sys import *
print('Hello, World!')
#addition function
def addition(a, b):
	print(a + b)
#subraction function
def subraction(a, b):
	print( a - b)
#dividion function
def division(a, b):
	print ( a / b)
#multiplication function
def multiplication(a, b):
	print (a * b)
#remainder function
def exponetion(a, b):
	print (a ** b)
#percentage function
def percentage(a, b):
	p = a/100
	print (a * b)
#BMI function
def BMI(a, b):
	bmi = a * b
	if bmi < 18.5:
		print (bmi)
		print ('Under-weight')
	elif bmi >=18.5 or bmi <=24.9:
		print (bmi)
		print ('Normal-weight')
	elif bmi > 25.0:
		print (bmi)
		print ('overweight')


#------------------------------------------#
print(''' need addition type('+')
		  need subtraction type ('-')
		  need division    type (' / ')
		  need multiplication   type (' * ')
		  need exponention type (' ^ ')
		  need percentage  type (' % ')
		  need need bmi    type (' bmi ')
	''')
while True:
	operation = input('Enter your operation you want to be done: ')
	if operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '^' or operation == '%' or operation == 'bmi':
		break
	print('type only the given attribute ')


if operation == '+':
	num1 = float(input('enter your first digit: '))
	num2 = float(input('enter your second digit: '))
	addition(num1, num2)

elif operation == '-':
	num1 = float(input('enter your first digit: '))
	num2 = float(input('enter your second digit: '))
	subraction(num1, num2)


elif operation == '*':
	num1 = float(input('enter your first digit: '))
	num2 = float(input('enter your second digit: '))
	multiplication(num1, num2)


elif operation == '/':
	num1 = float(input('enter your first digit: '))
	num2 = float(input('enter your second digit: '))
	division(num1, num2)

elif operation == '^':
	num1 = float(input('enter your first digit: '))
	num2 = float(input('enter your power to be multiplied to first number digit: '))
	exponetion(num1, num2)

elif operation == '%':
	num1 = float(input('enter your percentage of total digit: '))
	num2 = float(input('enter your total digit: '))
	percentage(num1, num2)
elif operation == 'bmi':
	num1 = float(input('Enter your weight'))
	num2 = float(input('Enter your heigh in meters'))
	num3 = float(num2 * num2)
	BMI(num1, num3)
else:
	print('Wrong Destination')
	exit()

''' This program is short non interactive
    python calculator 
    which is nearnly 100 lines of code
    also it used functions for single 
    operations 
    i've also included percentage and 
    bmi in this calculator which is a simple bmi; '''

input('your program ended')