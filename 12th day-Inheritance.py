class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    #   Class Constructor
   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
      def __init__(self,firstName,lastName,idNum,numScores):
        Person.__init__(self,firstName,lastName,idNum)
        self.numScores=numScores
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
      def calculate(self):
        sum=0
        for i in self.numScores:
            sum+=i
        avg = sum/len(self.numScores)   
        if (avg<=100 and avg >= 90):
            return "O"#outstanding
        elif (avg <= 90 and avg>= 80):
            return "E"#exceeds expectatitons
        elif(avg<=80 and avg >=70):
            return "A"#acceptable
        elif (avg<=70 and avg>=55):
            return "P"#poor
        elif (avg <= 55 and avg <= 40):
            return "D"#dreadful
        else:
            return "T" #troll


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())