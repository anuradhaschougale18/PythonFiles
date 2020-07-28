from A import *

class B(AA):
    def funB(self):
        print("I am method of class B...!")

class C(B):
    def funC(self):
        print("I am method of class C.....!")



def main():

    #object of class A can call own method
    a=AA()
    a.funA()

    #object of class B can call A,B
    b=B()
    b.funA()
    b.funB()

     #object of class A can call A,B,C
    c=C()
    c.funA()
    c.funB()
    c.funC()
    
if __name__=='__main__':
    main()
