from functools import reduce


# factorial : lambda x:x*= item for item in range(1,x+1)
factorial =lambda x:reduce(lambda a,b:a*b, [i for i in range(1, x)] )

reverse =lambda s:s[::-1]

print(reverse([1,2,4,6,8,5,3]))

filterEven= lambda lst: list(filter(lambda x:x%2==0, lst))