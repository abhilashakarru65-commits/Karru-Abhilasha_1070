import csv

# Writing data to CSV file
file = open("student.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow(["RollNo", "Name", "Sub1", "Sub2", "Sub3", "Sub4"])

writer.writerow([1, "Ram", 80, 85, 90, 88])
writer.writerow([2, "Sita", 75, 80, 85, 90])
writer.writerow([3, "Ravi", 90, 92, 95, 94])
writer.writerow([4, "Priya", 85, 88, 84, 86])
writer.writerow([5, "Arjun", 70, 75, 80, 78])
writer.writerow([6, "Sneha", 88, 90, 92, 89])
writer.writerow([7, "Kiran", 78, 82, 80, 79])
writer.writerow([8, "Anu", 95, 96, 94, 97])
writer.writerow([9, "Rahul", 82, 84, 86, 88])
writer.writerow([10, "Divya", 89, 91, 90, 92])

file.close()

# Reading and displaying records
file = open("student.csv", "r")
reader = csv.reader(file)

print("Student Records:")
for row in reader:
    print(row)

file.close()

# Finding highest scorer and average marks
file = open("student.csv", "r")
reader = csv.reader(file)
next(reader)

highest_name = ""
highest_total = 0
grand_total = 0
count = 0

for row in reader:
    total = int(row[2]) + int(row[3]) + int(row[4]) + int(row[5])

    if total > highest_total:
        highest_total = total
        highest_name = row[1]

    grand_total += total
    count += 1

print("\nHighest Scorer:", highest_name)
print("Total Marks:", highest_total)

average = grand_total / count
print("Average Marks of All Students:", average)

file.close()