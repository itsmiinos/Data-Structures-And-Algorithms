// Last updated: 8/13/2025, 8:21:52 PM
class MinStack {

    Stack<Long> s = new Stack();
    long min;

    public MinStack() {
        
    }
    
    public void push(int val) {
        if(s.size()==0){
            s.add((long)0);
            min = (long)val;
        }
        else{
            long diff = val - min;
            s.add(diff);
            if(diff<0){
                min = (long)val;
            }
        }
    }
    
    public void pop() {
        long val;
        if(s.peek()<0){
            val = s.pop();
            min = (long)min - val;
        }
        else{
            s.pop();
        }
    }
    
    public long top() {
        if(s.peek()<0){
            return (int)min;
        }
        return s.peek() + min;
    }
    
    public int getMin() {
        return (int)min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */