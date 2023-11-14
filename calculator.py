#!/usr/bin/python3
from Modules.process.py import *

print("""select the operation
1.Add
2.Subtract
3.Multiply
4.Division
5.Percentage
6.Exit
""")

while True:
	choice = input("Enter your choice (1/2/3/4/5/6): ")
	if choice in ('1','2','3','4','5','6'):

		number1 = float(input("Enter the first number: "))
		number2 = float(input("Enter the second number: "))

		if choice == "1":
			print("RESULT: {0} + {1} = {2}", format(number1,number2,add(number1,number2)))

		elif choice == "2":		
			print("RESULT: {0} - {1} = {2}", format(number1,number2,subtract(number1,number2)))

		elif choice == "3":
			print("RESULT: {0} * {1} = {2}", format(number1,number2,multiply(number1,number2)))

		elif choice == "4":
			print("RESULT: {0} / {1} = {2}", format(number1,number2,division(number1,number2)))
		elif choice == "5":
			print("RESULT: {0} % {1} = {2}", format(number1,number2,percentage(number1,number2)))
		elif choice == '6':
			exit()
		break
	else:
		print("invalid input")
