"""
Simple Interest  = (Principal_Amount * Rate * Time) /100
"""

principalAmount = float(input('Enter principal amount: '))
rateOfInterest = float(input('Enter rate of interest: '))
time = float(input('Enter time duration : '))

simpleInterest = (principalAmount * rateOfInterest *  time) /100

print(f"Simple Interest for the PrincipalAmount: {principalAmount}, RateOfInterest: {rateOfInterest}, Time Duration {time}, is {simpleInterest} ")

