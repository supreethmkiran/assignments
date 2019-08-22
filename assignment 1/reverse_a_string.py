"""reverse elements of a string without using theslicing operator [::-1]"""
l=eval(input("Enter a List of elements : "))
n=len(l)
for i in range(n//2):
    l[i],l[n-i-1]=l[n-i-1],l[i]
print(l)
"""
Enter a List of elements : [10,12,14,16,18,20]
[20, 18, 16, 14, 12, 10]
"""
