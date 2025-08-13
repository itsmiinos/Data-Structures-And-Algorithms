# Last updated: 8/13/2025, 8:16:58 PM
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_pair(s, a, b, value):
            stack = []
            score = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    score += value
                else:
                    stack.append(ch)
            return ''.join(stack), score

        if x > y:
            s, score1 = remove_pair(s, 'a', 'b', x)
            _, score2 = remove_pair(s, 'b', 'a', y)
        else:
            s, score1 = remove_pair(s, 'b', 'a', y)
            _, score2 = remove_pair(s, 'a', 'b', x)

        return score1 + score2
