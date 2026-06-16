lst1=[]

def lst_sq(lst):
    for l in lst:
        lst1.append(l**2)
    return lst1


# print(lst_sq([1,2,3,4,5,6,7,8]))


#list comprehension is a concise way to create lists. It consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. The expressions can be anything, meaning you can put in all kinds of objects in lists.
lst=[1,2,3,4,5,6,7,8]
print([i*i for i in lst]) #this is the same function but using list comprehension
print([i*i for i in lst if i%2==0]) #this is the same function but using list comprehension only for even numbers
