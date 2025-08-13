# Last updated: 8/13/2025, 8:21:46 PM
class MinStack:

    def __init__(self):
        self.stack = []
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        if len(self.stack) == 0 : 
            self.current_min = val
        diff = val - self.current_min
        self.stack.append(diff)
        if diff < 0 : 
            self.current_min = val

    def pop(self) -> None:
        popped = self.stack.pop(-1)
        if popped < 0 : 
            value = self.current_min
            self.current_min = self.current_min - popped
            return value
        return self.current_min + popped

    def top(self) -> int:
        top_value = self.stack[-1]
        if top_value < 0 : 
            return self.current_min
        else : 
            return self.current_min + top_value

    def getMin(self) -> int:
        return self.current_min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()