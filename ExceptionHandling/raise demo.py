'''
raisedemo
'''
def validate(age):
    if age<18:
        raise Exception("Invalid age for votting....!")
    else:
        print("congratulation you can vote")
try:
    validate(19)
except Exception as e:
    print(e)
