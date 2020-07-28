class Student:
    '''
__Rollno,__name,__course is private access specifier so we can  acces using class name
     #s1._student__course,rollno,name
'''

    def __init__(self):
         #private access specifier
        self.__rollno=input("Enter Roll no=>")
        #private access specifier
        self.__name=input("Enter Name=>")
        #private access specifier 
        self.__course=input("Enter Course=>")

    def printdata(self):
        print("Rollno=>",self.__rollno)
        print("Name=>",self.__name)
        print("Course=>",self.__course)

def main():

    s1=Student()
    s1.printdata()

    print("Access data outside of class")
    print("Rollno=>",s1._Student__rollno)
    print("Name=>",s1._Student__name)
    print("Course=>",s1._Student__course)
    #__Rollno,__name,__course is private access specifier so we can  acces using class name
     #s1._student__course,rollno,name

if __name__=='__main__':
    
    main()
    
