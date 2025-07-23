def custom_map(fun, items):
    return [fun(x) for x in items]

def custom_filter(fun, items):
    return [x for x in items if fun(x)]

def custom_reduce(fun, items):
    result=items[0]

    for val in items[1:]:
        fun(result,val)
    return result