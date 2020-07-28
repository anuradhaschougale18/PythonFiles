#polymorphism
class A():
    def __init__(self):
        print("consturctior of class A called......!")

    def msg(self):
        super().msg()
        print("Method of class A msgA")

class B():
    def __init__(self):
        print("consturctior of class B called......!")

    def msg(self):
       
        print("Method of class B msgB")

class C(A,B):
    def __init__(self):
        print("consturctior of class C called......!")

    def msg(self):
        super().msg()
        print("Method of class C msgC")


def main():
    c=C()
    c.msg()
    c.msg()
    c.msg()

if __name__=='__main__':
    main()
    
