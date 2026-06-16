#List is iterable

#Iterables are objects that can be iterated over, meaning that you can loop through them and access their elements one by one. 
# Examples of iterables include lists, tuples, strings, and dictionaries.

lst = [1,2,3,4,5,6,7,8]

lst1=iter(lst) #iter is a built-in function that returns an iterator object that can be used to iterate over the elements of the iterable
print(next(lst1)) #next is a built-in function that returns the next item from the iterator. If there are no more items to return, it raises a StopIteration exception.
print(next(lst1))