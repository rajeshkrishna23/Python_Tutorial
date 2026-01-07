#Task 2: Sum of Integers from 1 to 50 Using a Loop
#Problem Statement: Write a Python program that:
#1.Uses a for loop to iterate over numbers from 1 to 50.
#2.Calculates the sum of all integers in this range.
#3.Displays the final sum.
totalSum = 0
initialValue = int(input("Enter the number from which the sum should start: ")) #The first number of the range
finalValue = int(input("Enter the number up to which the sum should be calculated: ")) #The last number of the range

for number in range(initialValue,(finalValue+1)): # for each number in range of initial value till final value +1 as final value is exclusive
    totalSum += number # += is a shorthand operator which is similar to totalSum = totalSum+ number


print(f"The sum of numbers from 1 to 50 is {totalSum}")