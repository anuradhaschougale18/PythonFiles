'''
Task
A prime is a natural number greater than 1 that has no positive divisors
other than 1 and itself. Given a number,n , determine and print whether it's prime

or not prime .
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(n):
    if (n <= 1):
        return False

    for i in range(2,n):
        if (n%1==0):
            return False
    return True

n=int(input())
if isPrime(n):
    print("Prime")
else:
    print("Not Prime")
