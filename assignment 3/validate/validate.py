import random
import math


def otp():
    x=random.randint(1000,9999)
    print("the OTP is",x)
def captcha():
    q=random.randint(0,9)
    r=random.randint(65,90)
    d=random.randint(97,122)
    s=random.randint(0,256)
    if 65<=s>=90 or 97<=s>=122 or 48<=s>=57:
        y=random.randint(0,256)
        b=str(q)+chr(r)+chr(d)+chr(y)
        print(b)
    else:
        b=q+r+d+s
        print(b)
def eid():
    e=input("enter email id")
    if "@" in e and "." in e:
        if e.index("@")<e.index("."):
            print("email is valid")
        else:
            print("email is invalid")
    else:
        print("email is invalid")
    
otp()
captcha()
eid()
