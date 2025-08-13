// Last updated: 8/13/2025, 8:22:57 PM
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = 0;
        int p2 = 0;
        int p3 = 0;
        int[] ans = new int[m+n];
        while(p1<m && p2<n){
            if(nums1[p1]<nums2[p2]){
                ans[p3] = nums1[p1];
                p1++;
                p3++;
            }
            else{
                ans[p3] = nums2[p2];
                p2++;
                p3++;
            }
        }

        if(p1==m){
            while(p2<n){
                ans[p3] = nums2[p2];
                p2++;
                p3++;
            }
        }
        else{
            while(p1<m){
                ans[p3] = nums1[p1];
                p1++;
                p3++;
            }
        }

        for(int i=0;i<n+m;i++){
            nums1[i] = ans[i];
        }
    }
}