// Last updated: 8/13/2025, 8:21:16 PM
class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> p = new PriorityQueue();
        for(int i=0;i<k;i++){
            p.add(nums[i]);
        }
        for(int i=k;i<nums.length;i++){
            if(p.peek()<nums[i]){
                p.remove();
                p.add(nums[i]);
            }
        }
        return p.peek();
    }
}