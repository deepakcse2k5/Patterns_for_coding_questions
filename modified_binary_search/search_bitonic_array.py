def search_bitonic_array(arr, key):
    if len(arr)==0:
    return -1
  start , end = 0, len(arr)-1
  while start<=end:
   if 

    

def main():
   print(search_bitonic_array([1, 3, 8, 4, 3], 4))
   print(search_bitonic_array([3, 8, 3, 1], 8))
   print(search_bitonic_array([1, 3, 8, 12], 12))
   print(search_bitonic_array([10, 9, 8], 10))


main()
