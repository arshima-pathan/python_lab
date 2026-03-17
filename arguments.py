"""#basic positional arguments
def add (a,b):
    print("a=",a)
    print("b=",b)
    return a+b
result=add(2,5)    
print("sum=",result)

#student info
def studentinfo (name,roll,marks):
    print("name:",name)
    print("roll no:",roll)
    print("marks:",marks)
studentinfo("ravi",101,85)

#simple interest
def simple_interest (p,r,n):
    si=(p*r*n)/100
    print("simple interest:",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)

#area of circle
def ar_circle(r):
    a_circle=3.14*r*r
    print("area of circle:",a_circle)
    ar_circle(1.5)
    ar_circle(4)

#positive,negative or zero
def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")
        check_value(0)
        check_value(90)
        check_value(-15) 

#odd or even
def odd_even(no):
    if(no%2==0):
        print(f"value {no} is even")
    else:
        print(f"value {no} is odd")
        odd_even(50)
        odd_even(15)

#arithmatic operation substraction,multiplication,division
def addition (a,b):
    add=a+b
    print("addition of two values",add)
    addition(50,10.5)
    addition(100,200)



#basic keyword arguments
def studentinfo(name,age,city):
    print("name:",name)
    print("age:",age)
    print("city:",city)
    studentinfo(age=18,city="rajkot",name="ravi")

#mixing positional and keyword
def display(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    display(1,c=3,b=2)

#using keyword arguments
def simple_interest(p:float,r:int,t:float):
    si=(p*r*t)/100    
    print("simple interest:",si)
    simple_interest(p=10000,t=2,r=1.5)
    simple_interest(t=1.5,p=15000,r=2)
    
        
