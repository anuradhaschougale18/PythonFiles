'''

Given a string, S, of length N that is indexed from 0 to N - 1,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line (see the Sample below for more detail).
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
for i in range(n):
    s = input()
    s1 = list(s)
    l = len(s1)
    odd = ''
    even = ''
    for i in range(0,l):
        if i%2 == 0:
            even += str(s1[i])
        else:
            odd += str(s1[i])
    
    print (even, odd)
