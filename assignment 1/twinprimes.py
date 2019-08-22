n=int(input("Enter ending value for finding twin primes"))
l=list()
ctr=0
for i in range (2,n):
    a=i
    b=i+2
    
    for j in range(2,a):
        if(a%j==0):
            ctr = 1
    if(ctr==0):
        for j in range(2,b):
            if(b%j==0):
                ctr = 1
    if(ctr==0):
        l.append((a,b))
    ctr=0
print(l)
