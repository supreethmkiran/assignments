"""
usr1-pwd1
usr2-pwd2
usr3-pwd3
usr4-pwd4
usr5-pwd5
"""
f1=open("user.txt",'r')
a=input("Enter a Username :")
usr=list()
for i in range(5):
    s=f1.readline()
    p=s.index('-')
    usr.append(s[:p])
#print(usr)
f1.close()
f1=open("user.txt",'r')
pwd=list()
if (a in usr):
    passw=input("Enter the password :")
    posn=usr.index(a)
    for i in range(5):
        s=f1.readline()
        p=s.index('-')
        pwd.append(s[p+1:])
    if (pwd[posn]==passw+"\n"):
        print("Valid")
    else:
        print("Wrong Password")
"""
Enter a Username :usr1
Enter the password :pwd1
Valid
"""
