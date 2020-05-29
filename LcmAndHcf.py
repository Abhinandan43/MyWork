def Lcm(x,y):
    maximum=max(x,y)
    while(1):
        if(maximum%x==0 and maximum%y==0):
            print(' Lcm is ', maximum)
            break;
        maximum +=1
    
    Hcf= (x * y)/maximum
    print('Hcf is ', Hcf)

def main():
    n1=int(input("First Number "))
    n2=int(input("Second number"))
    z=Lcm(n1,n2)

if __name__=='__main__':
    main()
