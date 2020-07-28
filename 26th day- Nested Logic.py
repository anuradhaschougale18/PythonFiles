'''
Task
Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
If the book is returned after the calendar year in which it was expected, there is a fixed fine of .
'''

ad,am,ay=(int(y) for y in input().split())
ed,em,ey=(int(z) for z in input().split())
if (ay,am,ad)<=(ey,em,ed):
    print(0)
elif(am,ay)==(em,ey):
    print((ad-ed)*15)
elif(ay)==(ey):
    print((am-em)*500)
elif (ay)>(ey):
    print(10000)
