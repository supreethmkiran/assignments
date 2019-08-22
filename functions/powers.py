#Write a program to find the power of a number by recursion.
res=1
def power(x,y):
    global res
    if (y>0):
        res=res*x
        return power(x,y-1)
    else:
        return res
n=int(input("Enter a Number : "))
p=int(input("Enter the power of the number : "))
print (power(n,p))
"""
Enter a Number : 10
Enter the power of the number : 3
1000
"""
