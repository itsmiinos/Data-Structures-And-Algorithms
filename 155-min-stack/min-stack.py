class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_value = float('inf')

    def push(self, value: int) -> None:
        if len(self.my_stack) == 0 :
            self.min_value = value
            self.my_stack.append(0)
        else :
            diff = value - self.min_value
            self.my_stack.append(diff)

            if diff < 0 :
                self.min_value = value
        

    def pop(self) -> None:
        if self.my_stack[-1] < 0 :
            old_value = self.min_value
            self.min_value = self.min_value - self.my_stack[-1]
            self.my_stack.pop(-1)
            return old_value
        else :
            value = self.min_value + self.my_stack[-1]
            self.my_stack.pop(-1)
            return value

    def top(self) -> int:
        print(self.my_stack)
        if self.my_stack[-1] < 0 :
            return self.min_value
        else :
            return self.min_value + self.my_stack[-1]

    def getMin(self) -> int:
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()