#User function Template for python3

class Solution:
	def isNegativeWeightCycle(self, n, edges):
		#Code here
		
		ans = [0]*n
		ans[0] = 0
		
		for i in range(n-1) : 
		    for edge in edges : 
		        u = edge[0]
		        v = edge[1]
		        w = edge[2]
		        
		        if ans[u] + w < ans[v] : 
		            ans[v] = ans[u] + w
		            
		haveNegativeCycle = False
		for edge in edges : 
		        u = edge[0]
		        v = edge[1]
		        w = edge[2]
		        
		        if ans[u] + w < ans[v] : 
		            return 1
		return 0
		