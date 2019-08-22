from validate import otp,capthca,eid

print("for generating opt enter 1")
print('for generating captcha enter 2')
print('for verifying email id enter 3')

n=int(input("enter program no"))

while n>0:
    if i==1:
        validate.otp()
    elif i==2:
        validate.captcha()
    elif n==3:
        validate.eid()
    elif n==4:
        continue
    elif n==0:
        break
    n=int(input())
        
        
