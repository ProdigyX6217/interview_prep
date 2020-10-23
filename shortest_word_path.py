'''
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

{
"*it": [bit]
"b*t": [but]
"*ut":[but, put]
"p*t": [pot]
"po*": [pog, pot]
"*og": [dog, pog]
}


bit -> but -> put -> pot -> pog -> dog

bit 1
but 2
big 2

put 3
pot 4
lot 5
dog 6
'''

from collections import defaultdict, deque

def shortestWordEditPath(source, target, words):
  
  g = defaultdict(list)
  
  for word in words:
    for i in range(len(word)):
      key = word[:i]+"*"+word[i+1:]
      value = word
      g[key].append(word)
      
  print(g)
  
  q = deque([source])
  
  visited = []
  
  count = 0
      
  while q:
    
    node = q.popleft()
    
    
    for i in range(len(node)):
      
      s_key = node[:i]+"*"+node[i+1:]
      
      if s_key in g:

        
        for node_word in g[s_key]:
          
          if node_word == target:
            print (node_word, count)
            return count
          
          if node_word not in visited:
            q.append(node_word)
            visited.append(node_word)
    count += 1
    print (node, count)

            
  return -1
           
  
  

words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
source = "bit"
target = "dog"

print(shortestWordEditPath(source, target, words))

