def add(x,y):
	return x+y

def subtract(x,y):
	return x-y

def multiply(x,y):
	return x*y

def division(x,y):
	return x/y

print("""select the operation
1.Add
2.Subtract
3.Multiply
4.Division
""")

while True:
	choice = input("Enter your choice (1/2/3/4): ")
	if choice in ('1','2','3','4'):

		number1 = float(input("Enter the first number: "))
		number2 = float(input("Enter the second number: "))

		if choice == "1":
			print(number1, "+", number2, "=", add(number1,number2))

		elif choice == "2":		
			print(number1, "-", number2, "=", subtract(number1,number2))

		elif choice == "3":
			print(number1, "*", number2, "=", multiply(number1,number2))

		elif choice == "4":
			print(number1, "/", number2, "=", division(number1,number2))\

		break
	else:
		print("invalid input")
