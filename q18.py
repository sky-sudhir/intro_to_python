

from functools import reduce

upperText=map( str.upper,["hello","world"])
print(list(upperText))

def maxNum(v):
    return v<10


filterStr=filter(maxNum, [1,5,7,40,34,23,2])

print(list(filterStr))

def addNum(x,y):
    return x+y

reduceEle=reduce(addNum ,[item for item in range(1,20)])

print(reduceEle)