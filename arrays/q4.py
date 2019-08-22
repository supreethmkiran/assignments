#L=[[1,2,3,4],[5,6,7,8]]
L=eval(input("Enter a List of Lists : "))
x=len(L[0])
y=len(L)
L1=[[row[i] for row in L] for i in range(len(L[0]))]
#L1=[L[j][i] for i in range (x) for j in range(y)]
print(L)
print(L1)
"""
Enter a List of Lists : [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
[[1, 5, 9, 13, 17], [2, 6, 10, 14, 18], [3, 7, 11, 15, 19], [4, 8, 12, 16, 20]]
"""
