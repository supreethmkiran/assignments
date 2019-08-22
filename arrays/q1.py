l=[]
def trav(n):
    for i in n:
        print(i)
def insertionSort(arr): 
	for i in range(1, len(arr)): 
		key = arr[i] 
		j = i-1
		while j >=0 and key < arr[j] : 
				arr[j+1] = arr[j] 
				j -= 1
		arr[j+1] = key      
def inso (l,n):
    #l=l.sort()
    l.append(n)
    
    c=len(l)-1
    while (l[c-1]>=l[c] and c>=0):
        t=l[c]
        l[c]=l[c-1]
        l[c-1]=t
        c-=1
    print(l)
    return(l)
def biser(l,n):
    mi=0
    ma=len(l)
    mid=(mi+ma)//2
    pos=0
    while(mi<ma):
        if (n==l[mid]):
            pos=mid
            return(l[pos])
        elif(n<l[mid]):
            ma=mid-1
        elif(n>l[mid]):
            mi=mid+1
        mid=(mi+ma)//2
    if pos!=0:
        print('found')
    else:
        print('Not Found')
def inso (l,n):
    #l=l.sort()global l
    l.append(n)
    c=len(l)-1
    while (l[c-1]>l[c]):
        t=l[c]
        l[c]=l[c-1]
        l[c-1]=t
        c-=1
    print(l)
    return(l)
def dele(l,n):
    c=len(l)-1
    pos=0
    if n in l:
        while (n<=l[c]):
            pos=c
            c-=1
        #l[pos]=None
        l.pop(pos)
    print(l)
    return(l)



def lsor(a,b):
    na=len(a)
    nb=len(b)
    c=[]
    while (na>=0 and nb>=0):
        if a[na]>b[nb]:
            c.append(a[na])
            na-=1
        elif b[nb]>a[na]:
            c.append(b[nb])
            nb-=1
        elif b[nb]==a[na]:
            c.append(a[na])
            c.append(b[nb])
            nb-=1
            na-=1
    while (na>=0):
        c.append(a[na])
        na-=1
    while (nb>=0):
        c.append(b[nb])
        nb-=1
    return(c)
l=[1,2,3,4,5,6,7,8,9,10]
a=dele(l,5)
print(a)

