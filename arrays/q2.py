import q1
import datetime
l=[1,2,3,4,5,6,7,8,9,10]
#binary search
t1=datetime.datetime.now()
a=q1.biser(l,7)
t2=datetime.datetime.now()
bintime=t2-t1
#linear search
tl1=datetime.datetime.now()
a=0
n=7
flag=0
while a<len(l):
    if l[a]==n:
        flag=1
        break
    a+=1
tl2=datetime.datetime.now()
letime=tl2-tl1
print("time to find 7 in ",l,'using binary search',bintime)
print("time to find 7 in ",l,'using linear search',letime)
