x=input()
y=x.lower()
dna=['a','t','g','c']
rna=['a','g','c','u']
if(y=='a'):
    print('U')
elif(y=='t'):
    print('A')
elif(y=='c'):
    print('G')
elif(y=='g'):
    print('C')
else:
    print('Invalid input as a string')