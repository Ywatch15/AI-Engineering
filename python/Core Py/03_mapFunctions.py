def even_odd(n):
    if n%2==0:
        return "The given no {} is even".format(n)
    else:
        return "The given no {} is odd".format(n)


lst=[1,2,3,4,5,6,7,8,89,21,34,56,78,90]

result = list(map(even_odd, lst)) #map is a function that takes a function and an iterable and applies the function to each element of the iterable and returns a map object
print(result)
