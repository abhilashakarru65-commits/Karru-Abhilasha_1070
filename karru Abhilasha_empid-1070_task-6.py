# Simple Production Counter System

target = int(input("Enter target units: "))
workers = int(input("Enter workers per shift: "))
defect_rate = int(input("Enter defect rate (%): "))

total = 0
defects = 0

for shift in range(1, 4):

    print("\nShift", shift)

    for cycle in range(1, 21):

        for worker in range(1, workers + 1):

            # Defective item condition
            if worker % 5 == 0:
                print("Worker", worker, "- Defective item skipped")
                defects += 1
                continue

            total += 1
            print("Worker", worker, "- Item Produced")

            # Stop when target reached
            if total >= target:
                print("\nTarget Reached!")
                break

        if total >= target:
            break

    print("Total Produced so far:", total)
    print("Defects so far:", defects)

    if total >= target:
        break

print("\nFinal Production:", total)
print("Final Defects:", defects)