sum=0
prod=1
def cal(n):
    global sum,prod
    sum=sum+n
    prod*=n
ctr="y"
while (ctr=="y"):
    op=input("Do you want to Continue(y/n) : ")
    if (op=='y'):
        a=int(input("Enter a Number : "))
        cal(a)
    else:
        ctr="n"
        break
print("Product of the Entered Numbers : ",prod)
print("Sum of the Entered Numbers : ",sum)      
       
