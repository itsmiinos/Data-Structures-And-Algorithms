# Last updated: 2/11/2026, 9:56:03 PM
1class SegmentTree:
2    """Segment Tree over array of size n"""
3
4    def __init__(self, n: int):
5        self.n = n
6        self.size = 4 * n
7        self.sum = [0] * self.size
8        self.min = [0] * self.size
9        self.max = [0] * self.size
10
11    def _pull(self, node: int):
12        """Helper to recompute information of node by it's children"""
13
14        l, r = node * 2, node * 2 + 1
15
16        self.sum[node] = self.sum[l] + self.sum[r]
17        self.min[node] = min(self.min[l], self.sum[l] + self.min[r])
18        self.max[node] = max(self.max[l], self.sum[l] + self.max[r])
19
20    def update(self, idx: int, val: int):
21        """Update value by index idx in original array"""
22
23        def _update(node: int = 1, l: int = 0, r: int = self.n - 1):
24            if l == r:
25                self.sum[node] = val
26                self.min[node] = val
27                self.max[node] = val
28                return
29
30            m = l + (r - l) // 2
31            if idx <= m:
32                _update(node * 2, l, m)
33            else:
34                _update(node * 2 + 1, m + 1, r)
35
36            self._pull(node)
37
38        return _update()
39
40    def find_rightmost_prefix(self, target: int = 0) -> int:
41        """Find rightmost index r with prefixsum(r) = target"""
42
43        def _exist(node: int, sum_before: int):
44            return self.min[node] <= target - sum_before <= self.max[node]
45
46        def _find(node: int = 1, l: int = 0, r: int = self.n - 1, sum_before: int = 0):
47            if not _exist(node, sum_before):
48                return -1
49            if l == r:
50                return l
51
52            m = l + (r - l) // 2
53            lchild, rchild = node * 2, node * 2 + 1
54
55            # Check right half first
56            sum_before_right = self.sum[lchild] + sum_before
57            if _exist(rchild, sum_before_right):
58                return _find(rchild, m + 1, r, sum_before_right)
59
60            return _find(lchild, l, m, sum_before)
61
62        return _find()
63
64
65class Solution:
66    def longestBalanced(self, nums: List[int]) -> int:
67        n = len(nums)
68
69        stree = SegmentTree(n)  # SegmentTree over balance array for current l
70        first = dict()  # val -> first occurence idx for current l
71
72        result = 0
73        for l in reversed(range(n)):
74            num = nums[l]
75    
76            # If x already had a first occurrence to the right, remove that old marker.
77            if num in first:
78                stree.update(first[num], 0)
79
80            # Now x becomes first occurrence at l.
81            first[num] = l
82            stree.update(l, 1 if num % 2 == 0 else -1)
83
84            # Find rightmost r >= l such that sum(w[l..r]) == 0
85            r = stree.find_rightmost_prefix(target=0)
86            if r >= l:
87                result = max(result, r - l + 1)
88
89        return result