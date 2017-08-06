# This function should reverse the array passed in
# It has several bugs which you need to fix
def reverse(arr):
    # for each array index (from 0 to length of the array - 1)
    for i in range(len(arr)):
        #find the index i away from the end of the array
        pairIndex = len(arr) - i
        #swap the value at index i with its pair
        arr[i] = arr[pairIndex]
        arr[pairIndex] = arr[i]
    return arr


##### DO NOT MODIFY THESE LINES #####
# test the function with some arrays
print(reverse([2]))
#       should print [2]

print(reverse([2,4]))
#       should print [4,2]

print(reverse([1,7,2,20]))
#       should print [20, 2, 7, 1]

print(reverse([11,12,13,14,15]))
#        should print [15, 14, 13, 12, 11]
#####################################


### SOLUTION:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def reverse(arr):
    # for each array index (from 0 to length of the array - 1)
    arrCopy = arr[:]
    for i in range(len(arr)):
        #find the index i away from the end of the array
        pairIndex = len(arr) - i - 1
        #swap the value at index i with its pair
        temp0 = arr[pairIndex]
        temp1 = arr[i]
        arrCopy[i] = temp0
        arrCopy[pairIndex] = temp1
    return arrCopy


##### DO NOT MODIFY THESE LINES #####
# test the function with some arrays
print(reverse([2]))
#       should print [2]

print(reverse([2,4]))
#       should print [4,2]

print(reverse([1,7,2,20]))
#       should print [20, 2, 7, 1]

print(reverse([11,12,13,14,15]))
#        should print [15, 14, 13, 12, 11]
#####################################
