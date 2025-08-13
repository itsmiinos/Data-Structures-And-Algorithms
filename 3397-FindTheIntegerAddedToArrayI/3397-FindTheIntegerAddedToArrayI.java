// Last updated: 8/13/2025, 8:15:23 PM
class Solution {
    public int addedInteger(int[] nums1, int[] nums2) {
        int diff = 0;
        int n = nums1.length;
        for(int i=0;i<n;i++){
            diff = diff+(nums2[i] - nums1[i]);
        }
        return diff/n;
    }
}