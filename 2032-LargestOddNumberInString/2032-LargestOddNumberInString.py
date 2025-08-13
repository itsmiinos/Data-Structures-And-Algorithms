# Last updated: 8/13/2025, 8:16:48 PM
import sys
class Solution:
    def largestOddNumber(self, num: str) -> str:
        oddIndex = -1

        for i in range(len(num)-1 , -1 , -1) :
            if (int(num[i])%2!=0) :
                return num[0:i+1]
        return ""