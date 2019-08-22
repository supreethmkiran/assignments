#n=0
def fib(x,y,z):
   # global n
    if (z>0):
        c=x+y
        print(c,end=",")
        z-=1
        return fib(y,c,z)
    else:
        return 0
n=int(input("Enter Number of elements of the fibonacci series : "))
print('0')
print('1')
fib(0,1,n-2)
