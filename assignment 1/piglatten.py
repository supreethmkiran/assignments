n=input("Enter a Word : ")
l=list(n)
m=['a','e','i','o','u','A','E','I','O','U']
if(n[0] not in m):
    l.append(l[0])
    del(l[0])
    l.append('ay')
    for i in l:
        print(i,end="")
else:
    print(n +"yay")
"""
Enter a Word : Supreeth
upreethSay
"""
