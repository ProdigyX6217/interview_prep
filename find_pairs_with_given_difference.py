# function returns all (x,y) pairs in arr that equal to k
# y value in output must match order of the y element in the original array.

#input:  arr = [0, -1, -2, 2, 1], k = 1
#output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

def find_pairs_with_given_difference(arr, k):
  pairs = []
  set_custom = set()
  
  for num in arr:
    # [0, -1, -2, 2, 1]
    set_custom.add(num)
    # {0, -1, -2, 2, 1}
  
  for num in arr:
    y = num # setting y value to num(s) in arr
    x = y + k # finding x value from y and k
    if x in set_custom:
      pairs.append([x, y]) # appending all (x,y) pairs in arr that equal to k
   
  return pairs
        
    
#k = 1 
#x - y = k
#[[x, y], [x, y], [x, y]]


#x - y = 1
#y = [0, -1, -2, 2, 1]

#y = 0  x-0 = 1, 1-0 = 1, 
#x = 1
#[1, 0]


#y = -1, x - (-1) = 1, x = 1 + -1 = 0
#x = 0
#[0, -1]


#y = -2, x - (-2) = 1 , 
#x = -1
#[-1, -2]


#y = 2, x - 2 = 1, 
#x = null
# empty array


#y = 1, x - 1 = 1, 
#x = 2
#[2, 1]


#Output: [[1, 0], [0, -1], [-1, -2], [2, 1]]