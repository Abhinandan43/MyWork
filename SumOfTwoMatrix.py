row1=int(input("Enter length of row :\n"))
column1=int(input("Enter length of column :\n"))

row2=int(input("Enter length of row :\n"))
column2=int(input("Enter length of column :\n"))


matrix1=[]
matrix2=[]

for i in range(row1):
    a=[]  #because in python matrix is represented as [[1,2,3],[4,5,6]]
    for j in range(column1):
        a.append(int(input()))
    matrix1.append(a)

print()

for i in range(row2):
    b=[]  #because in python matrix is represented as [[1,2,3],[4,5,6]]
    for j in range(column2):
        b.append(int(input()))
    matrix2.append(b)

print()

for i in range(row1):
    for j in range(column1):
        print(matrix1[i][j],end=" ")
    print()

print()

for i in range(row2):
    for j in range(column2):
        print(matrix2[i][j],end=" ")
    print()

# Matrix Sum

result=[[0,0],[0,0]]  # change it as m*n

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j] + matrix2[i][j]

for r in result:
    print(r)