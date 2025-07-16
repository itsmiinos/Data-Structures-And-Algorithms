class StockSpanner:

    def __init__(self):
        self.stack = []
        self.curr_day = 0
        self.max_span = -float(inf)

    def next(self, price: int) -> int:
        if len(self.stack) == 0 : 
            self.stack.append([price , self.curr_day])
            self.curr_day +=1
            return 1
        
        difference = 0
        while len(self.stack) > 0 and self.stack[-1][0] <= price : 
            self.stack.pop(-1)
            if len(self.stack) > 0 : difference = self.curr_day - self.stack[-1][1]
            else : difference = self.curr_day+1
        
        self.stack.append([price , self.curr_day])
        self.curr_day+=1
        print(self.stack)
        return difference if difference > 0 else 1
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)