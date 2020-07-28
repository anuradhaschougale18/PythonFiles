class student:
    college='ITVEDANT'
    count=0
    def __init__(self,rollname,name):
        self.name=name
        self.rollno=rollname
        student.count=student.count+1
        print("total object=",student.count)
    def __del__(self):
        print("object destryed")
        
        student.count=student.count-1
        print("total object=",student.count)

    def printData(self):
        print("Rollno=",self.rollno)
        print("Name=",self.name)
        print("College=",student.college)

def main():
    s1=student(123,"Anu")
    s1.printData()
    s2=student(1234,"ruby")
    s2.printData()
    del s1

if __name__=='__main__':
    main()
