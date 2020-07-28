'''
finally
'''
try:
    print("hello")
    l=[10,20]
    print(l[5])
except Exception as e:
    print(e)
finally:
    print("I am finally will excute in both situation")
