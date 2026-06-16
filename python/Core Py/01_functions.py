# n=21
# if n%2==0:
#     print("even")
# else:
#     print("odd")


def even_odd(num):
    if num%2==0:
        print("even")
    else:
        print("odd")


# even_odd(32)

# n=int(input("Enter the number : "))
# even_odd(n)


#print vs return
    #this is print statement ex
# def hello():
#     print("hey")

# hello()

    #this is return statement ex
def hello():
    return "hey"

val=hello()
print(val)


def add_nums(n1,n2):
    return n1+n2
val=add_nums(7,9)
print(val)

def hey(name,age=22): #here name is positional argument and age is keyword arg
    print("Myself {} and age is {}".format(name,age))
hey('Sundu') 
hey('Sundu',21) #this will change the pre defined keyword argument



def sp(*args, **kwargs): #args are arguments, and kwargs are positional ones
    print(args)
    print(kwargs)
sp("Sundu", "Jii", age=22, dob=2004)



lst=[1,2,3,4,5,6,7,8]

def evenoddsum(lst):
    evens=0
    odds=0
    for l in lst:
        if l%2==0:
            evens+=l
        else:
            odds+=l

    return evens,odds

ans=evenoddsum(lst)
print(ans)