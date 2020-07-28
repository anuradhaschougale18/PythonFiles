from Bank import *

class ICICI(Bank):
    def __init__(self):
        print("welcome to ICICI")

class SBI(Bank):
    def __init__(self):
        print("Welcome to SBI")
class HDFC(Bank):
    def __init__(self):
        print("Welcome to HDFC")

def main():
    icici=ICICI()
    print("ICICI=>",icici.rateOfint(7.8,10000))


    sbi=SBI()
    print("SBI=>",sbi.rateOfint(8,10000))

    hdf=HDFC()
    print("HDFC=>",sbi.rateOfint(7,10000))


if __name__=='__main__':
    main()
