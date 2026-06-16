# def even_odd(n):
#     if n%2==0:
#         return "The given no {} is even".format(n)


lst = [1,2,3,4,5,6,7,8]

# result = list(filter(even_odd, lst)) #filter is a function that takes a function and an iterable and applies the function to each element of the iterable and returns a filter object that contains only the elements that satisfy the condition defined in the function
# print(result)


print(list(filter(lambda n:n%2==0, lst))) #this is the same function but using lambda