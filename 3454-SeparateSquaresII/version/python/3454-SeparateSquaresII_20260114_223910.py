# Last updated: 1/14/2026, 10:39:10 PM
1from typing import List
2import bisect
3
4
5class SegmentTree:
6    def __init__(self, xs: List[int]):
7        self.xs = xs
8        self.n = len(xs) - 1
9        self.count = [0] * (4 * self.n)
10        self.covered = [0] * (4 * self.n)
11
12    def update(self, qleft, qright, qval, left, right, pos):
13        if self.xs[right + 1] <= qleft or self.xs[left] >= qright:
14            return
15        if qleft <= self.xs[left] and self.xs[right + 1] <= qright:
16            self.count[pos] += qval
17        else:
18            mid = (left + right) // 2
19            self.update(qleft, qright, qval, left, mid, pos * 2 + 1)
20            self.update(qleft, qright, qval, mid + 1, right, pos * 2 + 2)
21
22        if self.count[pos] > 0:
23            self.covered[pos] = self.xs[right + 1] - self.xs[left]
24        else:
25            if left == right:
26                self.covered[pos] = 0
27            else:
28                self.covered[pos] = (
29                    self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]
30                )
31
32    def query(self):
33        return self.covered[0]
34
35
36class Solution:
37    def separateSquares(self, squares: List[List[int]]) -> float:
38        events = []
39        xs_set = set()
40        for x, y, l in squares:
41            events.append((y, 1, x, x + l))
42            events.append((y + l, -1, x, x + l))
43            xs_set.update([x, x + l])
44        xs = sorted(xs_set)
45
46        seg_tree = SegmentTree(xs)
47        events.sort()
48
49        psum = []
50        widths = []
51        total_area = 0.0
52        prev_y = events[0][0]
53
54        # scan: calculate total area and record intermediate states
55        for y, delta, xl, xr in events:
56            length = seg_tree.query()
57            total_area += length * (y - prev_y)
58            seg_tree.update(xl, xr, delta, 0, seg_tree.n - 1, 0)
59            # record prefix sums and widths
60            psum.append(total_area)
61            widths.append(seg_tree.query())
62            prev_y = y
63
64        # calculate the target area (half rounded up)
65        target = (total_area + 1) // 2
66        # find the first position greater than or equal to target using binary search
67        i = bisect.bisect_left(psum, target) - 1
68        # get the corresponding area, width, and height
69        area = psum[i]
70        width = widths[i]
71        height = events[i][0]
72
73        return height + (total_area - area * 2) / (width * 2.0)