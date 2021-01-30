def shifted_arr_search(shiftArr, num):
  for i in range(len(shiftArr)):
    if num == shiftArr[i]:
      return i
  return -1

