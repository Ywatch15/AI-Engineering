#Lambda functions are the anonymous functions with no name and are defined using the lambda keyword.
#They can take any number of arguments but can only have one expression.

#this is a normal function to add two numbers
def add(a,b):
    return a+b;

add=print(add(4,5))

# this is the same function but using lambda
lambda_add=lambda a,b:a+b
print(lambda_add(4,5))


even = lambda z:z%2==0
print(even(4))
print(even(5))