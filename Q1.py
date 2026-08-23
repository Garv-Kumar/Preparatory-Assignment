n = int(input("How many numbers do you want to enter? "))

maximum = int(input("Enter number 1: "))

for i in range(2, n + 1):
    number = int(input("Enter number " + str(i) + ": "))

    if number > maximum:
        maximum = number

print("Maximum number is:", maximum)