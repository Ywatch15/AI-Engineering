import numpy as np  #import inintially then be used

''' Understanding the 1D array basics
lst = [1,2,3,4,5,6]
arr=np.array(lst) #convert list to array
print(arr) #print the array
print(type(arr)) #print the type of arr
print(arr.shape) #print the shape of the array
print(arr.reshape(2,3))
'''

''' Understanding the 2D array basics
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]
arr2=np.array([l1,l2,l3]) #convert list of lists to array
print(arr2) #print the array
print(type(arr2)) #print the type of arr2
print(arr2.shape) #print the shape of the array
print(arr2.reshape(2,6)) #reshape the array to 2 rows and 6 columns
'''

'''
arr=np.array([1,2,3,4,5,6]) #create a 1D array
# print(arr[5])
arr2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) #create a 2D array
# print(arr2[1][2]) #print the element at row 1 and column
# print(arr2[1:2,0:3]) #print the first 2 rows and first 3 columns
# print(arr2[1:3,2:4]) #print the last 2 rows and last 2 columns is equivalent to print(arr2[1:,2:]) #print the last 2 rows and last 2 columns
arr3=np.arange(0,10,2) #create a 1D array with values from 0 to 10 with a step of 2
print(arr3) #print the array
arr4=np.linspace(1,10,50) #create a 1D array with values from 1 to 10 with 50 equally spaced values
print(arr4) #print the array
'''

arr= np.random.randint(0,100,10)
arr.sort() #sort the array in ascending order
print(arr) #print the array
arr2=arr.reshape(2,5) #reshape the array to 2 rows and 5 columns
arr2.sort() #sort the array in ascending order
print(arr2) #print the array after reshaping