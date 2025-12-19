"""
Amount = principalAmount(1+ Rate of Interest/100) ** T
compoundInterest = Amount-PrincipalAmount
"""
principalAmount = float(input('Enter principal amount: '))
rateOfInterest = float(input('Enter rate of interest: '))
time = float(input('Enter time duration : '))

# amount = principalAmount * (1+ rateOfInterest/100) ** time
amount = principalAmount * pow( (1+ rateOfInterest/100) , time)

compoundInterest = round(amount - principalAmount,2)

print(f"The compound interest for PrincipalAmount: {principalAmount}, RateOfInterest: {rateOfInterest}, Time: {time} is {compoundInterest}.")