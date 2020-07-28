class India:
    def getCapital(self):
        print("Delhi")
    def getCurrency(self):
        print("INR Rs. ")

class US:
    def getCapital(self):
        print("Washington Dc")

    def getCurrency(self):
        print("US $")

def main():
    i=India()
    us=US()

    for a in(i,us):
        a.getCapital()
        a.getCurrency()


if __name__=='__main__':
    main()
