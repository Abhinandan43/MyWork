# HCF of a number

def HCF(a,b):
    upper=[]
    for i in range(1,a+1):
        if a%i==0:
            upper.append(i)
    
    lower=[]
    for j in range(1,b+1):
        if b%j==0:
            lower.append(j)
    print(upper , "   ", lower)

    gcd=[]
    for m in upper:
        if m in lower:
            gcd.append(m)
    
    print(gcd[-1])
HCF(3,6)



# Method 2



def Hcf(a,b):
    minimum=min(a,b)
    cf=[]
    for i in range(1,minimum+1):
        if a%i==0 and b%i==0:
            cf.append(i)
    print(cf[-1])
Hcf(2,4)



# Method 3


def Gcd(a,b):
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            mrcf=i
    print(mrcf)
Gcd(2,4)



# Method 4


def Gcd(a,b):
    x=min(a,b)
    while x>0:
        if a%x==0 and b%x==0:
            return x
        else:
            x=x-1
print(Gcd(2,4))

