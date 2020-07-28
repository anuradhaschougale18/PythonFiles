class AgeInvalidError(Exception):
    pass

class candidate:
    def __init__(self,age):
        self.age=age

    def validate(self):
        try:
            if self.age<18:
                raise AgeInvalidError("Invalid age for votting......!")
            else:
                print("eligible for votting.....!")

        except AgeInvalidError as aie:
            print(aie)
def main():
        c1=candidate(12)
        c1.validate()

        c2=candidate(19)
        c2.validate()
main()
