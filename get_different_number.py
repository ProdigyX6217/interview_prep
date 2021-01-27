# Given an array arr of unique nonnegative integers, implement a function getDifferentNumber 
# that finds the smallest nonnegative integer that is NOT in the array.


def get_different_number(arr):  
  
  arr.sort()
  
  smallest = 0
  #[1, 3, 4, 5] <- 0
  #[0, 1, 2, 9] <- 3
  for i in range(len(arr)):
    if arr[i] == smallest:
      smallest += 1
      
    else:
      return smallest
    
  return smallest