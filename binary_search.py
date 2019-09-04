import random
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            c = True
            break
        else:
            c = False
    return c
data = [1, 2, 3, 4, 5, 6]
target = random.randrange(0, 10)
print("The list you have entered is", data)
print("The target value you want to match in the list is", target)
print(linear_search(data, target))