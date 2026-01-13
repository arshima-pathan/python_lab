"""#1. print message
print("HELLO WORLD")

#2. add two numbers
num1=float(input("ENTER THE FIRST NUMBER:"))
num2=float(input("ENTER THE FIRST NUMBER:"))
sum_result=num1+num2
print("the sum is:",sum_result)

#even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
    
#  check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
#print PI value
import math
print("The value of pi is:", math.pi)

#store & print constant value
PI = 3.14159  
print("The value of PI is:", PI)

#square of a number
number = float(input("Enter a number: "))
square = number ** 2
print(f"The square of {number} is {square}")

#area of circle
radius = float(input("Enter the radius of the circle: "))
area = 3.14159 * (radius ** 2)
print(f"The area of the circle is: {area}")

#check data type
a = 10              # Integer
b = 3.14            # Float
c = "Hello"         # String
d = [1, 2, 3]       # List
print(type(a))  
print(type(b))  
print(type(c))  
print(type(d)) 

#use math function
import math
# Trigonometry (Values are in Radians)
angle = math.radians(90) # Converts 90 degrees to radians
print(f"Sine of 90 degrees: {math.sin(angle)}")
# Logarithms
# Log of 100 with base 10
print(f"Log base 10 of 100: {math.log10(100)}")
# Absolute value (removes negative sign)
print(f"Absolute value of -15: {math.fabs(-15)}")

#find power
base = float(input("Enter the base: "))
exponent = float(input("Enter the exponent: "))
# Calculate power
result = base ** exponent
print(f"{base} raised to the power of {exponent} is: {result}") """

#check positive or nagative
num = float(input("Enter a number: "))
# Check the conditions
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

  