def Hcf(x,y):
    minimum=0
    hcf=0
    minimum=min(x,y)
    for i in range(1,minimum+1):
        if(x%i==0 and y%i==0):
            hcf=i
    print(hcf)

def main():
    n1=int(input('Enter first number'))
    n2=int(input('Enter first number'))
    z=Hcf(n1,n2)

if __name__ == '__main__':
    main()
