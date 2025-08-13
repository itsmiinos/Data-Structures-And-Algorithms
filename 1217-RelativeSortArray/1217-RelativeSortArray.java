// Last updated: 8/13/2025, 8:17:46 PM
class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] count = new int[1001];
        int ans[] = new int[arr1.length];
        for(int ele : arr1){
            count[ele]++;
        }
        
        int ansIndex = 0;
        for(int ele : arr2){
            while(count[ele]>0){
                ans[ansIndex] = ele;
                ansIndex ++;
                count[ele]--;
            }
        }

        for(int i=0;i<count.length;i++)
        {
            while(count[i]>0){
                ans[ansIndex] = i;
                count[i]--;
                ansIndex++;
            }
        }

        return ans;
    }
}