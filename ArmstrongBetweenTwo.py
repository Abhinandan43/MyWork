# Armstrong between two number

m=int(input("Enter initial limit : \n"))
n=int(input("Enter final limit : \n"))
lst=[]
for i in range(m,n+1):
    temp=i
    sum=0
    while temp >0:
        digit=temp%10
        sum=sum+digit**3
        temp=temp//10
    if sum==i:
        lst.append(i)
print(*lst)