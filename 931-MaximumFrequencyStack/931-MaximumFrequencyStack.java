// Last updated: 8/13/2025, 8:18:32 PM
class FreqStack {

    HashMap<Integer,Stack<Integer>> h = new HashMap();
    HashMap<Integer,Integer> f = new HashMap();
    int mf = 0;

    public FreqStack() {
        
    }
    
    public void push(int val) {
        int freq = f.getOrDefault(val,0);
        freq++;
        f.put(val,freq);
        if(h.containsKey(freq)==false){
            mf = Math.max(mf,freq);
            h.put(freq,new Stack());
        }
        h.get(freq).add(val);
    }
    
    public int pop() {
        int top =  h.get(mf).pop();
        int freq = f.get(top);
        freq--;
        f.put(top,freq);
        if(h.get(mf).size()==0){
            h.remove(mf);
            mf--;
        }
        return top;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */