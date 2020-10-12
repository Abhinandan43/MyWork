row1=int(input("Enter length of row :\n"))
column1=int(input("Enter length of column :\n"))

row2=int(input("Enter length of row2 :\n"))
column2=int(input("Enter length of column2 :\n"))

matrix1=[]
matrix2=[]

for i in range(row1):
    a=[]
    for j in range(column1):
        a.append(int(input()))
    matrix1.append(a)

print()

for i in range(row2):
    b=[]
    for j in range(column2):
        b.append(int(input()))
    matrix2.append(b)

for i in range(row1):
    for j in range(column1):
        print(matrix1[i][j],end=" ")
    print()

print()

for i in range(row2):
    for j in range(column2):
        print(matrix2[i][j],end=" ")
    print()

print()
# Multiplication step

result1=[[0,0],[0,0]] # for 2*2 matrix

result2=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            result1[i][j] += matrix1[i][k]*matrix2[k][j]
for r in result1:
    print(*r)