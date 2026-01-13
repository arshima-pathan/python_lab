#calculate simple intrest
p = float(input("Principal: "))
r = float(input("Rate: "))
t = float(input("Time: "))
print("Simple Interest:", (p * r * t) / 100)

#find maximum of 2 numbers
a = 10
b = 25
maximum = max(a, b)
print("The maximum number is:", maximum)

#print no. 1 to 5
for i in range(1, 6):
    print(i)
    
 #find length of a string
 text = "Hello World"
length = len(text)
print("The length of the string is:", length)

#print a wlcm message
print("Welcome to Python programming!")

#print first character of string
text = "Python"
first_char = text[0]
print("The first character is:", first_char) 

#print last character of string
text = "Python"
last_char = text[-1]
print("The last character is:", last_char)

#positive or nagative number
num = float(input("Enter a number: "))
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")
    
#add 3 numbers
a = 5
b = 10
c = 15
total = a + b + c
print("The sum is:", total)

#take a input from the user
name = input("Enter your name: ")
print(f"Hello, {name}!")