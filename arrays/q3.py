import q1
l=[1,2,3,4,5,6,7,8,9,10,11,12]
a=int(input("Enter a Number:"))
if(a in l):
        print("Element already exists")
else:
        q1.inso(l,a)
        #print(l)
"""
Enter a Number:15
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
"""

