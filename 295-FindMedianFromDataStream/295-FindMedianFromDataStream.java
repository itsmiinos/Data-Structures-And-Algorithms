// Last updated: 8/13/2025, 8:20:21 PM
class MedianFinder {

    PriorityQueue<Integer> left = new PriorityQueue(Collections.reverseOrder());
    PriorityQueue<Integer> right = new PriorityQueue();

    public MedianFinder() {
        
    }
    
    public void addNum(int num) {
        if(left.size()==right.size()){
            right.add(num);
            left.add(right.remove());
        }
        else{
            left.add(num);
            right.add(left.remove());
        }
    }
    
    public double findMedian() {
        if(left.size()==right.size()){
            return ((left.peek()+right.peek())/2.0);
        }
        else{
            return left.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */