def myMap(func,list):
    listA = []
    for x in list:
        listA.append(func(x))
        print(listA)
    return listA

def func(x):
    return x*5

myMap(func,[1,2,3,4,5])