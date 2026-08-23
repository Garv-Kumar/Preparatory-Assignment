strings = ["apple", "banana", "apple", "orange", "banana", "mango", "apple"]

duplicates = []

for item in strings:
    if strings.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Original list:")
print(strings)

print("Duplicate strings:")

for item in duplicates:
    print(item)
