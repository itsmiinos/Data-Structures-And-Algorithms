class Node:
    def __init__(self, val):
        self.val = val
        self.nextLetters = {}

class Solution:
    def countSubs(self, s):
        root = Node("")
        self.count = 0
        n = len(s)

        for i in range(n):
            curr = root
            for j in range(i, n):
                ch = s[j]
                if ch not in curr.nextLetters:
                    curr.nextLetters[ch] = Node(ch)
                    self.count += 1   # new distinct substring
                curr = curr.nextLetters[ch]

        return self.count