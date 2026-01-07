# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.

number =  int(input("Enter a number:\t")) # taking input from user and type casting it to integer

if number%2 == 0: # condition to check if the number is divisible by 2 % gives the remainder.If Remainder is =0 then the number is even else odd number
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
