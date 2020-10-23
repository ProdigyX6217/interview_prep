#https://docs.python.org/2/library/heapq.html
from heapq import heappush, heappop, heappushpop


def sort_k_messed_array(arr, k):
  
  new_arr = []
  
  result = []
  
  for i in range(len(arr)):
    
    if len(new_arr) <= k:
      heappush(new_arr, arr[i])
    else:
      result.append(heappushpop(new_arr, arr[i]))
  while new_arr:
    result.append(heappop(new_arr))
  return result
    
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
k =2

print(sort_k_messed_array(arr, k))


