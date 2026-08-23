names = []

n = int(input("How many student names do you want to enter (maximum 10): "))

if n > 10:
    n = 10

for i in range(n):
    name = input("Enter student name: ")
    names.append(name)

names.sort()

print()
print("Names in alphabetical order:")

for name in names:
    print(name)
