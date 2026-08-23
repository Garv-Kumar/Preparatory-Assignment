n = int(input("Enter the number of terms: "))

first = 0
second = 1

print("Fibonacci series:")

for i in range(n):
    print(first, end=" ")
    next_number = first + second
    first = second
    second = next_number

print()
