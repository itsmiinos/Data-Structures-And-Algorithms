// Last updated: 8/13/2025, 8:15:46 PM
class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer> h = new PriorityQueue(Collections.reverseOrder());
        int n = nums.length;
        long sum = 0;
        for(int i=0;i<n;i++){
            h.add(nums[i]);
        }

        while(k>0){
            int r = h.poll();
            sum = sum + r;
            h.add((int)Math.ceil(r/3.0));
            k--;
        }
        return sum;
    }
}