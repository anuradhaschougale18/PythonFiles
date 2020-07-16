'''
Task
Read a string, s, and print its integer value;
if s cannot be converted to an integer, print Bad String.
'''
import sys


S = input().strip()
try:
    print(int(S))
except ValueError:
    print("Bad String")
