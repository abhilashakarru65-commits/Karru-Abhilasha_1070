# Students Attendence Generator

total = int(input("Enter total classes: "))
present = int(input("Enter classes attended: "))

attendance = (present / total) * 100

print("Your attendance is", round(attendance, 2), "%")

if attendance >= 75:
    print("Good! You meet the attendance requirement.")
else:
    print("Warning! Attendance is below 75%.")