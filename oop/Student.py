class Student:
    def __init__(self):
        self.rollno=input("enter rollno=>")
        self.name=input("enter name=>")


    def printinformation(self):
        print("Rollno=",self.rollno)
        print("Name=",self.name)


def main():
        obj1=Student()
        print("datatype of obj1=",type(obj1))
        obj1.printinformation()
        print("********************")
        obj2=Student()
        print("datatype of obj2=",type(obj2))
        obj2.printinformation()
main()
