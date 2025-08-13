// Last updated: 8/13/2025, 8:24:45 PM
class Solution {
    PriorityQueue<Integer> left= new PriorityQueue(Collections.reverseOrder());
    PriorityQueue<Integer> right = new PriorityQueue();
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        for(int i=0;i<nums1.length;i++){
            addNum(nums1[i]);
        }
        for(int i=0;i<nums2.length;i++){
            addNum(nums2[i]);
        }
        return findMedian();


    }

    public void addNum(int n){
        if(left.size()==right.size()){
            right.add(n);
            left.add(right.remove());
        }
        else{
            left.add(n);
            right.add(left.remove());
        }
    }

    public double findMedian(){
        if(left.size()==right.size()){
            return ((left.peek()+right.peek())/2.0);
        }
        else{
            return left.peek();
        }
    }


}