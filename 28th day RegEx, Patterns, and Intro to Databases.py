'''
Task
Consider a database table, Emails, which has the attributes First Name
and Email ID. Given N rows of data simulating the Emails table,
print an alphabetically-ordered list of people whose email address ends in @gmail.com.
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    list =[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search("@gmail.com",emailID):
            list.append(firstName)
    list2=(sorted(list))
    for elem in list2:
        print(elem)

