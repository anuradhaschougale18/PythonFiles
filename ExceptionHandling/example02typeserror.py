def division(a,b):
    try:
        l=[10,20]
        x=int(input("Enter value in interger=>"))
        print(l[2])
        return(a/b)
    except ZeroDivisionError as ze:
        print(ze)
    except IndexError as ie:
        print(ie)
        
    except ValueError as vr:
        print(vr)
    
    except Exception as e:
        print(e)
    


print("division is=",division(10,2))
print("division is=",division(10,0))
print("division is=",division(10,4))
