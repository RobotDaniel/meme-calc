# Python program for simple calculator


# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
#check if 9+10 is entered
if select == 1 and number_1 == 9 and number_2 == 10:
	print(number_1,"+",number_2,"=",number_1 + number_2 + 2)


elif select == 1:
	print(number_1, "+", number_2, "=",number_1 + number_2)

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))
elif select == 1 and number_1 == 9 and number_2 == 10:
	print("9 + 10? =", 21)

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")
print("num1=", number_1, "num2=", number_2, "select=",select)
