# Last updated: 12/17/2025, 8:50:05 PM
1class Node :
2    def __init__(self , value) :
3        self.val = value
4        self.nextLetters = [-1 , -1]
5
6class Solution:
7    def findMaximumXOR(self, nums: List[int]) -> int:
8        root = Node("")
9        for i in range(len(nums)) :
10            self.createTrie(root , nums[i])
11        
12        max_xor = 0
13
14        for i in range(len(nums)) :
15            number = 0
16            curr = root
17            power = 31
18            for j in range(31 , -1 , -1) :
19                parity = (nums[i] >> j) & 1
20                parity_req = 1 - parity
21                if curr.nextLetters[parity_req] != -1 :
22                    number += (2 ** power)
23                    curr = curr.nextLetters[parity_req]
24                else :
25                    curr = curr.nextLetters[parity]
26
27                power -=1
28            
29            max_xor = max(max_xor , number)
30
31        return max_xor
32    
33
34
35    def createTrie(self , root : 'Node' , num : int) -> None :
36
37        curr = root
38        for i in range(31 , -1 , -1) :
39            parity = (num >> i) & 1
40            if curr.nextLetters[parity] != -1 :
41                node = curr.nextLetters[parity]
42                curr = node
43            else :
44                node = Node(parity)
45                curr.nextLetters[parity] = node
46                curr = node
47        
48