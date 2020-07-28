class A:
    def funA(self):
        print("I am method of class A..!")

class B(A):
    def funB(self):
        print("I am method of class B...!")

class C(B):
    def funC(self):
        print("I am method of class C.....!")



def main():

    #object of class A can call own method
    a=A()
    a.funA()

    b=B()
    b.funA()
    b.funB()

    c=C()
    c.funA()
    c.funB()
    c.funC()
    
if __name__=='__main__':
    main()
