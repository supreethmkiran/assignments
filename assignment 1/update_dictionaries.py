""" wap to merge 2 dictionairies"""
d1=eval(input("Enter a dictionary : "))
d2=eval(input("Enter another dictionary : "))
for i in d1:
    if (i in d2):
        d2[i]=d2[i]+d1[i]
    else:
        d2[i]=d1[i]
print(d2)
"""
Enter a dictionary{'a':10,'b':10,'c':10,'d':10,'e':10}
Enter another dictionary{'a':20,'c':20,'f':20,'e':10}
{'a': 30, 'c': 30, 'b': 10, 'e': 20, 'd': 10, 'f': 20}
"""
