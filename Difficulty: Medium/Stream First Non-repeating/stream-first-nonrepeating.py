from collections import deque

class Solution:
	def FirstNonRepeating(self, s):
		# Code here
		hashmap = {}
		queue = deque()
		result = ""
		
		for i in range(len(s)) : 
		    if s[i] not in hashmap : 
		        queue.append(s[i])
		        hashmap[s[i]] = 1
		    else : 
		        hashmap[s[i]] = hashmap.get(s[i]) + 1
		    
		    while len(queue) > 0 and hashmap[queue[0]] > 1 : 
		            queue.popleft()
		    
		    if len(queue) == 0 : 
		        result = result + "#"
		       
		    else : 
		        result = result + queue[0]
		return result