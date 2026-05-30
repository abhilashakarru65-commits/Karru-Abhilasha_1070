# Number Pattern Generator

n = int(input("Enter the value of n: "))

print("\n1. Right Triangle of Stars")
for i in range(1, n + 1):
    print("*" * i)

print("\n2. Inverted Triangle of Numbers")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n3. Pascal's Triangle")

for i in range(n):
    num = 1
    for j in range(n - i - 1):
        print(" ", end="")

    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()

print("\n4. Prime Numbers up to", n)

for num in range(2, n + 1):
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, end=" ")
