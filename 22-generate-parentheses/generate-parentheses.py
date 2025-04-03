class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def paranthesisRecursion(openN, closeN, currentString):
            if openN == closeN == n:  # Base case: Valid sequence completed
                res.append(currentString)
                return

            if openN < n:
                paranthesisRecursion(openN + 1, closeN, currentString + "(")

            if closeN < openN:
                paranthesisRecursion(openN, closeN + 1, currentString + ")")

        paranthesisRecursion(0, 0, "")
        return res