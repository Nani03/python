
import random
def linear_search():
    l=[]
    for x in range(5):
        l.append(random.randint(1,10))
    print(l)
    target = int(random.randint(1,10))
    print(a)
    for i in range(len(l)):
        if l[i] == target:
            print("true")
        else:
            print("false")

linear_search()




