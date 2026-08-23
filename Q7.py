first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

for number in range(first, second + 1):
    print()
    print("Multiplication table of", number)

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)
