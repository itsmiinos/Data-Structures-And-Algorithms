import sys
class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_till_now = sys.maxsize

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0 : 
            self.min_till_now = val
            diff = val - self.min_till_now
            self.min_stack.append(diff)
            
        else : 
            diff = val - self.min_till_now
            self.min_stack.append(diff)
            if diff < 0 : 
                self.min_till_now = val

    def pop(self) -> None:
        if len(self.min_stack) == 0 : return

        popped = self.min_stack.pop(-1)
        if popped < 0 : 
            self.min_till_now = self.min_till_now - popped

    def top(self) -> int:
        top = self.min_stack[-1]
        if top < 0 : 
            return self.min_till_now
        else : 
            return self.min_till_now + top

    def getMin(self) -> int:
        return self.min_till_now


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()