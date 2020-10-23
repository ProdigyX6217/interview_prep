# Python code to addition of two list sums 
 
# initializing arrays 
test_1 = [1, 3, 4, 6, 8] 
test_2 = [4, 5, 6, 2, 10] 
  
# printing original lists 
print ("List 1 : " + str(test_1)) 
print ("List 2 : " + str(test_2)) 
  
# add both arrays
res_list = [] 
for i in range(0, len(test_1)): 
    res_list.append(test_1[i] + test_2[i]) 
  
# printing third list  
print ("Final List : " + str(res_list)) 