#multiple
class A():
    def __init__(self):
        print("consturctior of class A called......!")

    def msgA(self):
        print("Method of class A msgA")

class B():
    def __init__(self):
        print("consturctior of class B called......!")

    def msgB(self):
        print("Method of class B msgB")

class C(A,B):
    def __init__(self):
        print("consturctior of class C called......!")

    def msgC(self):
        print("Method of class C msgC")


def main():
    c=C()
    c.msgA()
    c.msgB()
    c.msgC()

if __name__=='__main__':
    main()
    
