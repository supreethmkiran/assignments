def peri (l=1,b=1):
    p=2*(l+b)
    a=l*b
    return(p,a)
le=int(input("Enter the Length of the Rectangle"))
be=int(input("Enter the Breadth of the Rectangle"))
p,a=peri(le,be)
print("Perimeter = ",p,"Area : ",a)
