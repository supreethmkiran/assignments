
def mult(n):
    global ch
    if (n<=ch):
        print("7 * ",n,"= ",7*n)
        return mult(n+1)
    else:
        return 0
ch=int(input('Enter the number of desired multiples of 7 : '))
mult(1)
"""
Enter the number of desired multiples of 7 : 10
7 *  1 =  7
7 *  2 =  14
7 *  3 =  21
7 *  4 =  28
7 *  5 =  35
7 *  6 =  42
7 *  7 =  49
7 *  8 =  56
7 *  9 =  63
7 *  10 =  70
"""
