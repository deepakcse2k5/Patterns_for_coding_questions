arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

set1 = set(arr1)
set2= set(arr2)
set3 = set(arr3)

common_val = set1.intersection(set2).intersection(set3)
print(list(common_val))