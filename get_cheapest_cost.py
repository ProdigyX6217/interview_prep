def get_cheapest_cost(rootNode):
  # getting root node's children
  children = len(rootNode.children) 
  # getting the leaf node and its value
  if children == 0:
      return rootNode.cost
    
  minCost = float("inf") 
  # for each children node
  for i in range(children):
    tempCost = get_cheapest_cost(rootNode.i) 
    if tempCost < minCost :
      minCost = tempCost
  return minCost + rootNode.cost 


########################################## 
# Use the helper code below to implement #
# and test your function above           #
##########################################

#tree of nodes (distribution system)
#each node has a value, Looking for path that returns smallest sum
#leaf nodes are the last nodes in a path

# A node 
class Node:

  # Constructor to create a new node
  def __init__(self, cost):
    self.cost = cost
    self.children = []
    self.parent = None
