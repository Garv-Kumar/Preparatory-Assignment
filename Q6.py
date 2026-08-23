rows1 = int(input("Enter rows of first matrix: "))
cols1 = int(input("Enter columns of first matrix: "))

matrix1 = []

print("Enter first matrix:")
for i in range(rows1):
    row = []
    for j in range(cols1):
        value = int(input("Enter element: "))
        row.append(value)
    matrix1.append(row)

rows2 = int(input("Enter rows of second matrix: "))
cols2 = int(input("Enter columns of second matrix: "))

matrix2 = []

print("Enter second matrix:")
for i in range(rows2):
    row = []
    for j in range(cols2):
        value = int(input("Enter element: "))
        row.append(value)
    matrix2.append(row)

if cols1 != rows2:
    print("Matrix multiplication is not possible.")
else:
    result = []

    for i in range(rows1):
        row = []
        for j in range(cols2):
            total = 0
            for k in range(cols1):
                total = total + matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    print("Resulting matrix:")
    for row in result:
        print(row)
