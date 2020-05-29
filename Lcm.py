def Lcm(x,y):
    maximum=0
    maximum=max(x,y)
    while(1):
        if maximum%x==0 and maximum%y==0:
            print('Lcm ', maximum)
            break
        maximum +=1

def main():
    n1=int(input('Enter first number'))
    n2=int(input('Enter second number'))
    z=Lcm(n1,n2)
if __name__ =='__main__':
    main()
