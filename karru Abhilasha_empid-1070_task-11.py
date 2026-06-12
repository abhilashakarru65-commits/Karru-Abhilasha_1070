# ==================================
# BUG 1 - RUNTIME ERROR
# ==================================
# Type   : IndexError
# Reason : Wrong list position
# Fix    : Use a valid position

print("BUG 1 - RUNTIME ERROR")

try:
    marks = [80, 75, 90, 65, 85]
    print(marks[5])   # Buggy Code
except IndexError as e:
    print("Error:", e)

# Fixed Code
print("Fixed Output:", marks[0])


# ==================================
# BUG 2 - LOGICAL ERROR
# ==================================
# Type   : Logical Error
# Reason : Wrong average formula
# Fix    : Divide by total students

print("\nBUG 2 - LOGICAL ERROR")

total = sum(marks)

# Buggy Code
wrong_average = total / 4
print("Wrong Average:", wrong_average)

# Fixed Code
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Correct Average:", average)
print("Total Marks:", total)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)