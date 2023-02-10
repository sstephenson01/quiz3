#Quiz 3
#The Authors' are Olivia Busk and Sarah Stephenson

# Problem 5
def net_value(salary):
    value=0.14*(salary-100)+0.24*(salary+1000)
    print("The value is", value)

net_value(200)

# Problem 6
def next_stop(location):
    print("The next stop is",  location)
    print("The next stop is",  location)

next_stop("South Bend")

# Problem 7
import math
def circle(radius):
    area=math.pi*(radius)**2
    circumference=2*math.pi*radius
    print("The difference between the area and the circumference is", area-circumference)

circle(5)

# Problem 8
def hello(name):
    print("Hello,", name)

hello("Olivia and Sarah")

# Problem 9
def answer(x):
    value=(math.sin(x)**3)+math.cos(x)-3*((math.tan(x))/(math.tan(x)+1)**2)
    print(value)
answer(9)
