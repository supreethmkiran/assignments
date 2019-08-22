a=input("Enter a Letter : ")
b= ord(a)
if(b<=90 and b>=65):
    b=b+32
else:
    b=b-32
print(chr(b))
