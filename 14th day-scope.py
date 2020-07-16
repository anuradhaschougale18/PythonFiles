'''
Complete the Difference class by writing the following:

A class constructor that takes an array of integers as a parameter and
saves it to the instance variable.
A computeDifference method that finds the maximum absolute difference
between any numbers in and stores it in the instance variable.
'''


class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        sorted_elements = sorted(self.__elements)
        self.maximumDifference = abs(sorted_elements[-1] - sorted_elements[0])

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
