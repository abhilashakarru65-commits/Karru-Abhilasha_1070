#Creating a bill-Splitting calculator
total_bill = float(input("Enter total bill amount : "))
no_of_people = int(input("Enter Number of people :"))
tip_percentage = float(input("Enter tip percentage :"))

tip_amount = (total_bill * tip_percentage) / 100
total_amt_with_tip = total_bill + tip_amount
amount_per_person = total_amt_with_tip / no_of_people

remainder_check = total_bill % no_of_people

tip_amount = round(tip_amount, 2)
total_with_tip = round(total_amt_with_tip, 2)
amount_per_person = round(amount_per_person, 2)

# Output 
print("\n----- ----------Bill Summary --------------------------")
print("Original Bill: ₹", total_bill)
print("Tip Amount: ₹", tip_amount)
print("Total with Tip: ₹", total_with_tip)
print("Amount Per Person: ₹", amount_per_person)
print("Remainder when bill is divided:", remainder_check)
print("---------------------------------------------------------")