number = int(input("Enter Number: "))

binary = bin(number)[2:]
octal = oct(number)[2:]
hexadecimal = hex(number)[2:].upper()

print("Given Number:", number)
print("Binary equivalent:", binary)
print("Octal equivalent:", octal)
print("Hexadecimal equivalent:", hexadecimal)
