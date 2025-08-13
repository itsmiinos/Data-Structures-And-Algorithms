// Last updated: 8/13/2025, 8:19:25 PM
class Solution {
    public int subarraySum(int[] nums, int k) {
        HashMap<Integer,Integer> h = new HashMap();
        int pNums[] = new int[nums.length];
        int ans = 0;
        h.put(0,1);
        pNums[0] = nums[0];
        for(int i=1;i<nums.length;i++){
            pNums[i] = pNums[i-1] + nums[i];
        }

        for(int ep=0;ep<nums.length;ep++){
            int sp = pNums[ep] - k;
            System.out.println(sp);
            ans += h.getOrDefault(sp,0);
            h.put(pNums[ep],h.getOrDefault(pNums[ep],0)+1);
        }
        return ans;
    }
}