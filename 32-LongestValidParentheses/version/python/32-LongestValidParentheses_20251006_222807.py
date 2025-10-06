# Last updated: 10/6/2025, 10:28:07 PM
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]      # base for valid substring
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)    # new base
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
