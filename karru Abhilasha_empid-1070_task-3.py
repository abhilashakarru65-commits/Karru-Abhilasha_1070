#Enhanced Loan Eligibility System
user_age = int(input("Enter your age: "))
user_salary = int(input("Enter your salary: "))
job = input("Enter employment type: ").lower()

if user_age < 21 or user_age > 60:
    print("Age not eligible")

elif user_salary < 25000:
    print("Salary not eligible")

elif job != "salaried" and job != "self-employed":
    print("Wrong employment type")

elif 21 <= user_age <= 30 and user_salary < 30000:
    print("Guarantor required")

elif user_age > 55 and job == "self-employed":
    print("Need senior approval")

else:
    print("Loan Approved")
