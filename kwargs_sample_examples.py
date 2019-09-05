#Kwargs to convert regular variables to dicts
def my_three(a, b, c):
    print(a, b, c)
a = {'a': "one", 'b': "two", 'c': "three"}
my_three(10,11,12)
my_three(**a)

#passing dynamic arguments
def dynamicDict(**dict):
    for key, value in dict.items():
        print("{} is {}".format(key,value))
dynamicDict(Firstname="Krishna", Lastname="KL", Age=24, Phone=102910298)

dynamicDict(Firstname="Venky", Lastname="L", Age=24, Phone=12679812738)
