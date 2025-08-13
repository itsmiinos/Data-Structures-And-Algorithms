# Last updated: 8/13/2025, 8:21:06 PM
class Solution:
    def calculate(self, s: str) -> int:
        operators = []
        operands = []

        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue

            if s[i] == '-' and self.is_unary(i, s):
                i += 1
                while i < len(s) and s[i] == ' ':
                    i += 1
                if i < len(s) and s[i] == '(':
                    operands.append(0)
                    operators.append('-')
                    continue
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                operands.append(-num)
                i -= 1

            elif s[i].isdigit():
                number = 0
                while i < len(s) and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1
                operands.append(number)
                i -= 1

            elif s[i] in ['+', '-', '*', '/']:
                while (operators and operators[-1] != '(' and
                       self.precedence(operators[-1]) >= self.precedence(s[i])):
                    operand_two = operands.pop()
                    operand_one = operands.pop()
                    operator = operators.pop()
                    ans = self.calculation(operand_one, operand_two, operator)
                    operands.append(ans)
                operators.append(s[i])

            elif s[i] == '(':
                operators.append(s[i])

            elif s[i] == ')':
                while operators and operators[-1] != '(':
                    operand_two = operands.pop()
                    operand_one = operands.pop()
                    operator = operators.pop()
                    ans = self.calculation(operand_one, operand_two, operator)
                    operands.append(ans)
                operators.pop()  # Remove '('

            i += 1

        while operators:
            operand_two = operands.pop()
            operand_one = operands.pop()
            operator = operators.pop()
            ans = self.calculation(operand_one, operand_two, operator)
            operands.append(ans)

        return operands[0]

    def is_unary(self, i: int, s: str) -> bool:
        if i == 0:
            return True
        j = i - 1
        while j >= 0 and s[j] == ' ':
            j -= 1
        return j < 0 or s[j] in '(-+*/'

    def calculation(self, a: int, b: int, c: str) -> int:
        if c == '+':
            return a + b
        elif c == '-':
            return a - b
        elif c == '*':
            return a * b
        elif c == '/':
            return int(a / b)  # truncate toward zero

    def precedence(self, c: str) -> int:
        if c in ('*', '/'):
            return 2
        elif c in ('+', '-'):
            return 1
        return 0
