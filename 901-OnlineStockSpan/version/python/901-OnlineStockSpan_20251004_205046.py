# Last updated: 10/4/2025, 8:50:46 PM
class StockSpanner:

    def __init__(self):
        self.current_day = 0
        self.stack = []

    def next(self, price: int) -> int:
        difference = 0
        if len(self.stack) == 0 : 
            self.stack.append([price , self.current_day])
            self.current_day +=1
            return 1
        
        while len(self.stack) > 0 and self.stack[-1][0] <= price : 
            self.stack.pop(-1)
            if len(self.stack) > 0 : difference = self.current_day - self.stack[-1][1]
            else : difference = self.current_day+1
        
        self.stack.append([price , self.current_day])
        self.current_day+=1
        print(self.stack)
        return difference if difference > 0 else 1



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)