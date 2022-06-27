import imp


import os

folder = os.walk('Z:\\Новая папка')
newAr = []

def show():
    for ad, dir, file, in folder:
        newAr.append(file)
    print(newAr)
# show()

def arTry(*args):
    new_list = []
    for i in args:
        for y in i:
            if y not in new_list:
                new_list.append(y)
    return new_list

z = ['a','b','c',2,2]
x = [2,3,5,6,7,7]

print(arTry(z,x))
def newFunc(arr1, arr2):
    return arr1+arr2

newArr = newFunc(2,3)
# print(newArr)