from array import *
arr1 = array('i', [1,2,3,4,5]);
arr2 = array('d', [1.2,3.4,5.6]);

# print(arr1)
# print(arr2)


# lets insert a new element int end of first array
# syntax: arrayName.insert(index, value)
arr1.insert(6,7)
# print(arr1)

# adding the new element in the begining
# note that in the above example we added in the last so the time complexity was constant but now we will have a 'n' complexity

arr1.insert(0,0)
print(arr1)