// Last updated: 8/13/2025, 8:17:51 PM
class Solution {
    public int heightChecker(int[] heights) {
        int n = heights.length;
        int ans = 0;
        int count[] = new int[101];

        for(int height : heights){
            count[height]++;
        }

        int j = 0;
        for(int i=0;i<n;i++){
            while(j<count.length && count[j]==0){
                j++;
            }
            if(heights[i]!=j){
                ans++;
            }
            count[j]--;
        }
        return ans;



        // for(int i=0;i<n;i++)
        // {
        //     expected[i] = heights[i];
        // }
        // Arrays.sort(heights);

        // for(int i=0;i<n;i++){
        //     if(heights[i]!=expected[i]){
        //         count++;
        //     }
        // }
        //return count;
    }
}