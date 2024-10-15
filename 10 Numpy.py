print('      NUMPY        ')
print('===================')
print(' ')
# import numpy as np
# print(dir(np))

## NUMPY CREATING ARRAYS ##

# import numpy as np
# array = np.array([1,2,3,4,6])
# print(array)
# print(type(array))

# import numpy as np
# array = np.array({1, 2, 3, 4, 6})
# print(array)
# print(type(array))

# import numpy as np
# print(np.__version__)

# to check the dimension of the array
# import numpy as np
# a = np.array([1,3,4,5])
# print(a.ndim)

# import numpy as np
# a = np.array([[1,2,3,5,6,7]])
# print(a.ndim)

# import numpy as np
# a = np.array([[[1,2,3,5,6,7]]])
# print(a.ndim)

# # to check the shape of the array
# import numpy as np
# a = np.array([1,3,4,5])
# print(a.shape)

# to check the data type of the array
# import numpy as np
# a = np.array([1,3,4,5])
# print(a.dtype) #int32

# import numpy as np
# a = np.array([1.3,3,4.5,5])
# print(a.dtype) #float64


## When the array is created, you can define the number of dimensions by using the ndmin argument
## Create an array with 5 dimensions and verify that it has 5 dimensions:

# import numpy as np
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print('number of dimensions :', arr.ndim)

## to change the data type
# import numpy as np
# a = np.array([1,3,4,2],dtype ='f')
# print(a) #[1. 3. 4. 2.]

# import numpy as np
# a = np.array([1,3,4,2],dtype ='S')
# print(a) #[b'1' b'3' b'4' b'2']

# import numpy as np
# arr = np.array(['a', '2', '3'], dtype='i')
# print(a)  #error

## conversion from one data type to other
# import numpy as np
# a = np.array([1,2,4,3])
# b = a.astype('S')
# print(b)

# import numpy as np
# arr = np.array([1.1, 2.1, 3.7])
# newarr = arr.astype(int)
# print(newarr)
# print(newarr.dtype)

# ============== revision ==========
# import numpy as np
# arr = np.array([1,2,3,4,5,6])
# print(arr)
# print(arr.ndim)
# print(arr.dtype)
# newarr = arr.astype('S')
# print(newarr)
# newarr = arr.astype('f')
# print(newarr)
# newarr = arr.astype('i')
# print(newarr)

# import numpy as np
# arr = np.array([1,2,3,4,5,6],dtype = 'f')
# print(arr)
# arr = np.array([1,2,3,4,5,6],dtype = 'S')
# print(arr)



#============ 16-09-24 ==============
# import numpy as np
# arr = np.array([[-1, 0, 1],[1,2,3]])
# newarr = arr.astype(bool)
# print(newarr)
# print(arr.shape)
# # [[ True False  True]
# #  [ True  True  True]]
# # (2, 3)

## Copy => it is the new arr from original array
## View => it is just a view of the original array

# # Copy =>
# import numpy as np
# arr = np.array([1,2,3,4,5])
# print(f'Array before copy: {arr}')
# newarr = arr.copy()
# arr[0] = 32
# print(f'Copied array: {newarr}')
# print(f'Original array after changes: {arr}')

# print('=====================')

# # # View =>
# import numpy as np
# arr = np.array([1,2,3,4])
# print(f'Array before view: {arr}')
# newarr = arr.view()
# arr[0] = 32
# print(f'View array: {newarr}')
# print(f'Original array after changes: {arr}')

## "base" attribute in numpy
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.

# import numpy as np
# arr = np.array([1,2,3,4])

# a = arr.copy()
# b = arr.view()

# print(a.base) #copy => owns data
# print(b.base) #view  => does not owns data

## 'Shape' is th attribute in numpy gives you the order of your array in the form if (rows , column)

# import numpy as np
# arr = np.array([[1,2,3,4],[4,6,5,7]])
# newarr = arr.shape
# print(f'Shape of the array:{newarr}')
# print(f'Rows:{newarr[0]}, Columns:{newarr[1]} ')#(2, 4)

## The example above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

# # Q-Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4.

# import numpy as np
# arr = np.array([1,2,3,4],ndmin =5)
# print(arr)
# print(f'Shape of that array: {arr.shape}')

# # Output => (1, 1, 1, 1, 4)
# What does the shape tuple represent?
# Integers at every index tells about the number of elements the corresponding dimension has.

# In the example above at index-4 we have value 4, so we can say that 5th ( 4 + 1 th) dimension has 4 elements.

## Reshaping arrays
# 1.Reshaping means changing the shape of an array.
#
# 2.The shape of an array is the number of elements in each dimension.
#
# 3.By reshaping we can add or remove dimensions or change number of elements in each dimension.

#=========Reshape From 1-D to 2-D=========
# Q-Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:

## arr.reshape(number of arrays, number of elements in the array

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# newarr = arr.reshape(4,3)
# print('Original array:',arr)
# print('New array is:',newarr)

## Output is
# Original array: [ 1  2  3  4  5  6  7  8  9 10 11 12]
# New array is: [[ 1  2  3]
#                [ 4  5  6]
#                [ 7  8  9]
#                [10 11 12]]

#=========Reshape From 1-D to 3-D=========
# Q - Convert the following 1-D array with 12 elements into a 3-D array.
# The outermost dimension will have 2 arrays that contains 3 arrays, each with 2 elements:

# # arr.reshape(Number of array1,number of arrays inarray1,number of elements in each array)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)

# # Output is
# [[[ 1  2]
#   [ 3  4]
#   [ 5  6]]

#  [[ 7  8]
#   [ 9 10]
#   [11 12]]]


## Can We Reshape Into any Shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.

# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.

#Q-Example : Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)

# # Output => ValueError: cannot reshape array of size 8 into shape (3,3)

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8,9])
# newarr = arr.reshape(3, 3)
# print(newarr)

# # Output => [[1 2 3]
#              [4 5 6]
#              [7 8 9]]

# Q-Example => Check if the returned array is a copy or a view:

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# print('Dimension of original array is:',arr)
# print(arr.reshape(4,2).base))

# The example above returns the original array, so it is a view.

## Magic of reshaping Unknown Dimension
## Pass '-1' s the value, and NumPy will calculate this number for you.

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,2,-1))

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(2,-1,2))

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(-1,2,2))

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# print(arr.reshape(-1,-1,-1))
## Output = ValueError: can only specify one unknown dimension

##  Note: We can not pass -1 to more than one dimension.


## Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

# import numpy as np
# arr = np.array([[1, 2, 3], [4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)

# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.


#============17-09-24==============

# import numpy as np
# arr = np.array([1,2,3,4,5])
#
# for x in arr:
#     print(x)

################# 3-10-24 ###################

##How to concatenate two arrays
##axis = row 1  and column 0

## Theory => Joining means putting contents of two or more arrays in a single array.
#In SQL we join tables based on a key, whereas in NumPy we join arrays by axes.
#We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.

# import numpy as np
# arr1= np.array([[1,3,4,2],[5,6,7,8]])
# arr2 = np.array([[9,10,11,12],[13,14,15,16]])
# result = np.concatenate((arr1,arr2),axis=1)
# print(result)

## output =>
#[[ 1  3  4  2  9 10 11 12]
#[ 5  6  7  8 13 14 15 16]]

#-----------------------------------------------
##Joining Arrays Using Stack Functions
##Stacking is same as concatenation, the only difference is that stacking is done along a new axis.

##We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

##We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0.


# import numpy as np
# arr1= np.array([[1,3,4,2],[5,6,7,8]])
# arr2 = np.array([[9,10,11,12],[13,14,15,16]])
# result = np.stack((arr1,arr2),axis=1)
# print(result)

#-----------------------------------------------
## Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.

# import numpy as np
# arr1= np.array([[1,3,4,2],[5,6,7,8]])
# arr2 = np.array([[9,10,11,12],[13,14,15,16]])
# result = np.hstack((arr1,arr2))
# print(result)
#
# Output =>
# [[ 1  3  4  2  9 10 11 12]
#  [ 5  6  7  8 13 14 15 16]]

#----------------------------------------------
# Stacking Along Columns
# NumPy provides a helper function: vsstack() to stack along columns.

# import numpy as np
# arr1= np.array([[1,3,4,2],[5,6,7,8]])
# arr2 = np.array([[9,10,11,12],[13,14,15,16]])
# result = np.vstack((arr1,arr2))
# print(result)

# Output =>
# [[ 1  3  4  2]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]


#--------------------------------------------
# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

# import numpy as np
# arr1= np.array([[1,3,4,2],[5,6,7,8]])
# arr2 = np.array([[9,10,11,12],[13,14,15,16]])
# result = np.dstack((arr1,arr2))
# print(result)

#-----------------------------------------
#NUMPY Splitting array

# import numpy as np
# arr1 = np.array([1,2,3,4,5,6])
# arr = np.array_split(arr1,3)
# print(arr)

#----------------------------------------
#NUMPY Array Search

# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(arr == 4)
# print(x)

#-----------------------------------------------
##Find the indexes where the values are even:

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 0)
# print(x)

# (array([1, 3, 5, 7], dtype=int64),)

#-------------------------------------------------
##Find the indexes where the values are odd:

# import numpy as np
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# x = np.where(arr%2 == 1)
# print(x)

# (array([0, 2, 4, 6], dtype=int64),)

#------------------------------------------------
# NumPy Sorting Arrays
# Sorting means putting elements in an ordered sequence.

# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.

# The NumPy ndarray object has a function called sort(), that will sort a specified array.

# import numpy as np
# arr = np.array([3, 2, 0, 1])
# print(np.sort(arr))

# import numpy as np
# arr = np.array(['banana', 'aherry', 'apple'])
# print(np.sort(arr))

# import numpy as np
# arr = np.array([True, False, True])
# print(np.sort(arr))

# import numpy as np
# arr = np.array([[3, 2, 4], [5, 0, 1]])
# print(np.sort(arr))

#--------------------------------------------
# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

# In NumPy, you filter an array using a boolean index list.

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7,8])
# filter_array =arr > 4
# newarr = arr[filter_array]

# print(filter_array)
# print(newarr)

# [False False False False  True  True  True  True] ##Boolean index list
# [5 6 7 8]


#-------------------------------------------------
# Creating the Filter Array
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

# import numpy as np
#
# arr = np.array([34,21,56,78,43,57,89,21])
#
# filter_arr =[]
#
# for element in arr:
#
#     if element > 50:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
#
# newarr = arr[filter_arr]
#
# print(newarr)
# print(filter_arr)

#-----------------------------------------
# Creating Filter Directly From Array

# import numpy as np
#
# arr = np.array([41, 42, 43, 44])
#
# filter_arr = arr > 42
#
# newarr = arr[filter_arr]
#
# print(filter_arr)
# print(newarr)

#---------------------------------------
int i = 1, j = 1 ;
    for(; i<= 10; i++)
    {
        if(i%3 != 0) { j += 2; continue;}
        if(j%3 == 0)  break;
    }
printf("%d",i+j);