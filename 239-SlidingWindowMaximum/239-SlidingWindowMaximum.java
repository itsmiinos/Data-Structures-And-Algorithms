// Last updated: 8/13/2025, 8:20:45 PM
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque();
        int n = nums.length;
        int ans[] = new int[n-k+1];

        for(int i=0;i<k;i++){
            while(q.size()>0 && nums[i]>q.getLast()){
                q.removeLast();
            }
            q.addLast(nums[i]);
        }
        ans[0] = q.getFirst();

        for(int i=k;i<n;i++){
            if(nums[i-k]==q.getFirst()){
                q.removeFirst();
            }
            while(q.size()>0 && nums[i]>q.getLast()){
                q.removeLast();
            }
            q.addLast(nums[i]);
            ans[i-k+1] = q.getFirst();
        }

        return ans;
    }
}