text = input("Enter a string: ")

uppercase = 0
lowercase = 0
digits = 0
other = 0

for ch in text:
    if ch >= 'A' and ch <= 'Z':
        uppercase = uppercase + 1
    elif ch >= 'a' and ch <= 'z':
        lowercase = lowercase + 1
    elif ch >= '0' and ch <= '9':
        digits = digits + 1
    else:
        other = other + 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Other characters:", other)
