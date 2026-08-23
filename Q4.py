marks = []

for i in range(5):
    mark = int(input("Enter marks for subject " + str(i + 1) + " out of 20: "))
    marks.append(mark)

total = 0

for mark in marks:
    total = total + mark

if total >= 90:
    grade = "Ex"
elif total >= 80:
    grade = "A"
elif total >= 70:
    grade = "B"
elif total >= 60:
    grade = "C"
else:
    grade = "F"

print("Total marks:", total)
print("Grade:", grade)
