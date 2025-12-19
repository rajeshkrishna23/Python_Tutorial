"""Task 1: Perform Basic Mathematical Operations
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

firstNumber = int(input('Enter first number: '))
secondNumber = int(input('Enter second number: '))

Sum = firstNumber + secondNumber
Difference = firstNumber - secondNumber
Product = firstNumber * secondNumber
quotient = firstNumber / secondNumber

print(f"Addition: {Sum}\nSubtraction: {Difference}\n Multiplication: {Product}\n Division: {quotient}")