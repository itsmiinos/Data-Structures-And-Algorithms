// Last updated: 8/13/2025, 8:24:50 PM
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        HashMap<Integer,Integer> h = new HashMap();
        for(int i=0;i<n;i++){
            int num = nums[i];
            if(h.containsKey(target-num)){
                return new int[] {i,h.get(target-num)};
            }
            h.put(num,i);
        }
        return new int[] {};
    }
}