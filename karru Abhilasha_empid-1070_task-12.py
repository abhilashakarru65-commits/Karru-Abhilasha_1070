
# =============================================================
# DAY 1 - VARIABLES, DATA TYPES, INPUT/OUTPUT, OPERATORS
# =============================================================


# -------------------------------------------------------------
# 1Q. Program to Find the Sum of Two Numbers
# -------------------------------------------------------------

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum =", num1 + num2)

print("=" * 60)


# -------------------------------------------------------------
# 2Q. Program to Calculate Area of a Rectangle
# -------------------------------------------------------------

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)

print("=" * 60)


# -------------------------------------------------------------
# 3Q. Program to Calculate Simple Interest
# -------------------------------------------------------------

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time period: "))

interest = (principal * rate * time) / 100

print("Simple Interest =", interest)

print("=" * 60)


# -------------------------------------------------------------
# 4Q. Program to Convert Celsius to Fahrenheit
# -------------------------------------------------------------

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Temperature in Fahrenheit =", fahrenheit)

print("=" * 60)


# -------------------------------------------------------------
# 5Q. Program to Calculate HRA (20%) and DA (10%)
# -------------------------------------------------------------

basic_salary = float(input("Enter basic salary: "))

hra = basic_salary * 0.20
da = basic_salary * 0.10

print("HRA =", hra)
print("DA =", da)

print("=" * 60)



# =============================================================
# DAY 2 - CONDITIONS
# =============================================================


# -------------------------------------------------------------
# 6Q. Program to Check Positive, Negative or Zero
# -------------------------------------------------------------

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

print("=" * 60)


# -------------------------------------------------------------
# 7Q. Program to Find Largest Among Two Numbers
# -------------------------------------------------------------

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)

print("=" * 60)


# -------------------------------------------------------------
# 8Q. Program to Find Largest Among Three Numbers
# -------------------------------------------------------------

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

if x >= y and x >= z:
    print("Largest =", x)
elif y >= x and y >= z:
    print("Largest =", y)
else:
    print("Largest =", z)

print("=" * 60)


# -------------------------------------------------------------
# 9Q. Program to Check Whether a Number is Even or Odd
# -------------------------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

print("=" * 60)


# -------------------------------------------------------------
# 10Q. Program to Check Whether a Year is Leap Year
# -------------------------------------------------------------

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

print("=" * 60)



# =============================================================
# DAY 3 - LOOPS
# =============================================================


# -------------------------------------------------------------
# 11Q. Program to Print Numbers from 1 to 100
# -------------------------------------------------------------

for i in range(1, 101):
    print(i)

print("=" * 60)


# -------------------------------------------------------------
# 12Q. Program to Print Even Numbers Between 1 and 100
# -------------------------------------------------------------

for i in range(2, 101, 2):
    print(i)

print("=" * 60)


# -------------------------------------------------------------
# 13Q. Program to Find Sum of First N Natural Numbers
# -------------------------------------------------------------

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

print("=" * 60)


# -------------------------------------------------------------
# 14Q. Program to Print Multiplication Table
# -------------------------------------------------------------

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("=" * 60)


# -------------------------------------------------------------
# 15Q. Program to Calculate Factorial of a Number
# -------------------------------------------------------------

n = int(input("Enter a number: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)

print("=" * 60)



# =============================================================
# DAY 4 - FUNCTIONS
# =============================================================


# -------------------------------------------------------------
# 16Q. Program to Find Square of a Number Using Function
# -------------------------------------------------------------

def square(num):
    return num * num

n = int(input("Enter a number: "))

print("Square =", square(n))

print("=" * 60)


# -------------------------------------------------------------
# 17Q. Program to Find Maximum of Two Numbers Using Function
# -------------------------------------------------------------

def maximum(a, b):
    if a > b:
        return a
    return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Maximum =", maximum(a, b))

print("=" * 60)


# -------------------------------------------------------------
# 18Q. Program to Calculate Simple Interest Using Function
# -------------------------------------------------------------

def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter Principal Amount: "))
r = float(input("Enter Rate of Interest: "))
t = float(input("Enter Time Period: "))

print("Simple Interest =", simple_interest(p, r, t))

print("=" * 60)


# -------------------------------------------------------------
# 19Q. Program to Check Even or Odd Using Function
# -------------------------------------------------------------

def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

n = int(input("Enter a number: "))

print(check_even_odd(n))

print("=" * 60)


# -------------------------------------------------------------
# 20Q. Program to Calculate Area of Circle Using Function
# -------------------------------------------------------------

def area_circle(radius):
    return 3.14 * radius * radius

r = float(input("Enter radius: "))

print("Area of Circle =", area_circle(r))

print("=" * 60)



# =============================================================
# DAY 5 - LISTS, TUPLES, DICTIONARY, SET
# =============================================================


# -------------------------------------------------------------
# 21Q. Program to Create a List of 10 Numbers and Print Elements
# -------------------------------------------------------------

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("List Elements:")

for i in numbers:
    print(i)

print("=" * 60)


# -------------------------------------------------------------
# 22Q. Program to Find Largest Element in a List
# -------------------------------------------------------------

print("Largest Element =", max(numbers))

print("=" * 60)


# -------------------------------------------------------------
# 23Q. Program to Calculate Sum of All Elements in a List
# -------------------------------------------------------------

print("Sum of Elements =", sum(numbers))

print("=" * 60)


# -------------------------------------------------------------
# 24Q. Program to Count Even Numbers in a List
# -------------------------------------------------------------

count = 0

for i in numbers:
    if i % 2 == 0:
        count += 1

print("Number of Even Elements =", count)

print("=" * 60)


# -------------------------------------------------------------
# 25Q. Program to Remove Duplicate Elements Using Set
# -------------------------------------------------------------

data = [1, 2, 2, 3, 4, 4, 5, 6, 6]

unique_data = list(set(data))

print("Original List =", data)
print("List After Removing Duplicates =", unique_data)

print("=" * 60)
