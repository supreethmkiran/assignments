vl=['a','e','i','o','u','A','E','I','O','U']
nl=['1','2','3','4','5','6','7','8','9','0']
cap=0
vo=0
sp=0
nu=0
def check(n):
    global cap,vo,sp,nu
    if ((ord(n)>=65 and ord(n)<=90) or (ord(n)>=97 and ord(n)<=122)):
        if(ord(n)>=65 and ord(n)<=90):
            cap+=1
        if(n in vl):
            vo+=1
    elif(n in nl):
        nu+=1
    else:
        sp+=1
st=input("Enter a String : ")
for i in range(len(st)):
    a=st[i]
    check(a)
print("Numbers : ",nu)
print("Vowels : ",vo)
print("Capital Letters : ",cap)
print("Special Characters : ",sp)
