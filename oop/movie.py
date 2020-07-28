class movie:
    def __init__(self):
        print("object created")
        self.name=str()
        self.year=str()

    def __del__(self):
        print("object desroyed")

    def loadInfo(self):
        self.name=input("Enter movie name=>")
       self.year=input("Enter year of release movie=>")

    def printInfo(self):
        print("Movie name=",self.name)
        print("Movie Year=",self.year)


def main():
    m1=movie()
    print(m1.name,':',m1.year)
    m1.loadInfo()
    m1.printInfo()
    del m1 
    m2=movie()
    print(m2.name,':',m2.year)
    m2.loadInfo()
    m2.printInfo()

if __name__=='__main__':
    main()
