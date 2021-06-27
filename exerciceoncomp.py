def foo(lists):
    result = [listme for listme in lists if isinstance(listme, int)]
    return result
print(foo[99, 'no data', 98, 90])
