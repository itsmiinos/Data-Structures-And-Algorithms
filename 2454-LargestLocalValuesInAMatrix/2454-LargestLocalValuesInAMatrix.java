// Last updated: 8/13/2025, 8:16:02 PM
class Solution {
    public int[][] largestLocal(int[][] grid) {
        int[][] ans = new int [grid.length-2][grid.length-2];
        for(int i=0;i<ans.length;i++){
            for(int j=0;j<ans[i].length;j++){
                ans[i][j]=largestLocalHelper(i,j,grid);
            }
        }
        return ans;
    }

    public int largestLocalHelper(int l,int m,int[][]grid){
        int max = Integer.MIN_VALUE;
        for(int i=l;i<l+3;i++){
            for(int j=m;j<m+3;j++){
                max = Math.max(max,grid[i][j]);
            }
        }
        return max;
    }
}