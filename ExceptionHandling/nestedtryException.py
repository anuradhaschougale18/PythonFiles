'''
Nested try block
'''

def calc():
    try:
        try:
            x=int(input("Enter value=>"))
            y=int(input("Enter value=>"))
            a=x/y
            print("Answer is=",a)
        except ZeroDivisionError as ze:
            print(ze)

        try:
             l=[10,20]
             i=int(input("Enter index to get element value=>"))
             print(l[i])
        except IndexError as ie:
             print(ie)
    except Exception as e:
        print(e)
