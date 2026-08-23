text = input("Enter a string: ")

counts = {}

for ch in text:
    if ch.isalpha():
        ch = ch.upper()

        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1

print("Alphabet occurrences:")

for ch in sorted(counts):
    print(ch, ":", counts[ch])
