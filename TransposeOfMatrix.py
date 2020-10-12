m=int(input("Enter length of row :\n"))
n=int(input("Enter length of column :\n"))

matrix=[]

for i in range(m):
    a=[]
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

print()
print("Original Matrix :")
for i in range(m):
    for j in range(n):
        print(matrix[i][j],end=" ")
    print()

print("Transpose Matrix :")

for i in range(m):
    for j in range(n):
        print(matrix[j][i],end=" ")
    print()