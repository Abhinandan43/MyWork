limit=int(input("Enter limit : "))
n1=0
n2=1
count=2
if limit<=0:
    print("Enter positive Number")
elif limit==1:
    print(n1)
else:
    print("Fibonacci Sequence :")
    print(n1,n2, end=",")
    while count<limit:
        nth =n1 + n2
        print(nth,end= ",")
        n1=n2
        n2=nth
        count=count + 1
