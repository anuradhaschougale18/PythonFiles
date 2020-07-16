'''
Given an array, A, of N integers, print each element in
reverse order as a single line of space-separated integers.
'''
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(*reversed(arr))
