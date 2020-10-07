def PrimeBetween():
    m=int(input("Enter initial limit "))
    n=int(input("Enter final limit "))
    for i in range(m,n+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i, end=" ")
PrimeBetween()