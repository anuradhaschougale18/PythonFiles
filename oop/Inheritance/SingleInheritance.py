class A:
    def __init__(self):
        self.name=str()
    def printHi(self):
        self.name=input("Enter name=>")
        print(self.name,"Hi........!")

        
class B(A):
    def printHello(self):
        print(self.name,"Hello......!")

def main():
    a=A()
    a.printHi()

    b=B()
   # b.printHi()
    b.printHello()

if __name__=='__main__':
    main()
