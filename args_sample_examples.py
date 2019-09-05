#Simple example of passing multiple arguments using *args
def myFun(arg1, *args):
    print("argument 1 is : ", arg1)
    for arg in args:
        print("through args :", arg)

myFun('Hello', 'How', 'are', 'you?')

#adding multiple varables using *args

def add(*args):
    x=0
    for num in args:
        x+= num
    print(x)
add(10,20,50)
add(40,50,20,10,90)

#multiplication of variables using args

def multiply(*args):
    x=1
    for num in args:
        x *= num
    print(x)

multiply(10,20,30)


