# Last updated: 2/15/2026, 8:12:08 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        return bin(int(a, 2) + int(b, 2))[2 : ]