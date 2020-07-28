class student:
    college='ITVEDANT'
    
    def __init__(self,rollname,name):
        self.name=name
        self.rollno=rollname
    def __del__(self):
        print("object destryed")        

    def printData(self):
        print("Rollno=",self.rollno)
        print("Name=",self.name)
        print("College=",student.college)

  
def main():
    s1=student(123,"Anu")
    s1.printData()
    s2=student(1234,"ruby")
    s2.printData()
   
if __name__=='__main__':
    main()
