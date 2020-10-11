def BinaryToDecimal(num):
    base=1
    decimal=0
    while num>0:
        remainder=num%10
        decimal=decimal+remainder*base
        num=num//10
        base=base*2
    return decimal
print(BinaryToDecimal(101))

