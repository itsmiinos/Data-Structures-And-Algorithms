class Solution:
    def InfixtoPostfix(self, s: str) -> str:
        def precedence(op):
            if op == '^':
                return 3
            elif op in '*/':
                return 2
            elif op in '+-':
                return 1
            else:
                return 0

        output = []
        stack = []

        for ch in s:
            if ch.isalnum():  # Operand (letter or digit)
                output.append(ch)

            elif ch == '(':
                stack.append(ch)

            elif ch == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # pop '('

            elif ch in '+-*/^':
                while (stack and stack[-1] != '(' and
                       precedence(stack[-1]) >= precedence(ch)):
                    output.append(stack.pop())
                stack.append(ch)

        while stack:
            output.append(stack.pop())

        return ''.join(output)
