def shifted_arr_search(shiftArr, num):
  # shiftArr=   [9, 12, 17, 2, 4, 5], num = 12
  #index = shiftArr[i]
  #shiftArr[i] == num ?
  # O(n) means the work you do is proportional to input
  # O(1) means the work you do is independent to input
  for i in range(len(shiftArr)):
    
    # i = 1
    # if 12 == shiftArr[1]
    # if 12 == 12
    if num == shiftArr[i]:
      return i
  return -1

  # binary search on input
  # have to handle special case where shiftArr[i] < shiftArr[i-1]
  
    
    
print(shifted_arr_search([9, 12, 17, 2, 4, 5], 17))
  
  