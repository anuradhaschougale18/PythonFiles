class Student:

    def __init__(self):
        #public access specifier
        self.rollno=input("Enter Roll no=>")
        #protected access specifier
        self._name=input("Enter Name=>")
        #private access specifier 
        self.__course=input("Enter Course=>")

    def printdata(self):
        print("Rollno=>",self.rollno)
        print("Name=>",self._name)
        print("Course=>",self.__course)

def main():

    s1=Student()
    s1.printdata()

    print("Access data outside of class")
    print("Rollno=>",s1.rollno)
    print("Name=>",s1._name)
    print("Course=>",s1.__course)
    #__course is private access specifier so we can  not access bcz it is private access specifier
if __name__=='__main__':
    main()
    
