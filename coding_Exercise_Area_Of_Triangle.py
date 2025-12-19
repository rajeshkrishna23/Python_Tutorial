"""Area of a Triangle
when all the sides are known say a,b,c
semi perimeter = (a+b+c)/2
Area_Of_Triangle = (s * (s-a)*(s-b)*(s-c))
"""
sideA = int(input('Enter first side: '))
sideB= int(input('Enter second side: '))
sideC= int(input('Enter third side: '))
semiPerimeter = ((sideA+sideB+sideC)/2) # Calculation of semi perimeter
areaOfTriangle = round((semiPerimeter * (semiPerimeter-sideA)*(semiPerimeter-sideB)*(semiPerimeter-sideC))) # Calculation of area of triangle.
print(f"The area of triangle for the sideA: {sideA}, sideB: {sideB}, sideC: {sideC} is :{areaOfTriangle} ")