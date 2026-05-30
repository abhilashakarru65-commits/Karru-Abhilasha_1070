# TAX Generator

income = float(input("Enter your annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
else:
    tax = income * 0.10

print("Tax Amount =", tax)


