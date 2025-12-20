# Last updated: 12/21/2025, 12:28:06 AM
1class Node :
2    def __init__(self , value) :
3        self.val = value
4        self.nextBits = [-1 , -1]
5
6class Solution:
7    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
8        que = []
9        for i in range(len(queries)) :
10            que.append([queries[i][0] , queries[i][1] , i])
11        que.sort(key = lambda x : x[1])
12        nums.sort()
13        root = Node("")
14        i = 0
15        result = [0]*len(que)
16        for u , v , a in que :
17            max_xor = 0
18            while i < len(nums) and nums[i] <= v:
19                self.createTrie(root , nums[i])
20                i+=1
21            
22            if i == 0:
23                result[a] = -1
24                continue
25            
26            curr = root
27            power = 31
28            xor = 0
29            for k in range(31 , -1 , -1) :
30                bit = ( u >> k ) & 1
31                bit_req = 1 - bit
32                
33                if curr.nextBits[bit_req] != -1:
34                    xor += 2 ** power
35                    curr = curr.nextBits[bit_req]
36                else :
37                    curr = curr.nextBits[bit]
38
39                power -=1
40            max_xor = max(xor , max_xor)
41            
42            result[a] = max_xor
43        
44        return result
45
46
47    def createTrie(self , root : 'Node' , n : int) -> None :
48        curr = root
49
50        for i in range(31 , -1 , -1):
51            parity = (n >> i) & 1
52            if curr.nextBits[parity] != -1:
53                curr = curr.nextBits[parity]
54            else :
55                node = Node(parity)
56                curr.nextBits[parity] = node
57                curr = node