// Last updated: 8/13/2025, 8:17:36 PM
class Solution {
    int row[] = {-1, 0, 0, 1};
        int col[] = {0, -1, 1, 0};

    public int getMaximumGold(int[][] grid) {
        int maxSum = Integer.MIN_VALUE;
        int n = grid.length;
        int m = grid[0].length;
        int i = 0;
        int j = 0;
        int ans = 0;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                if(grid[i][j]!=0){
                    ans = Math.max(ans,dfsHelper(i,j,grid));
                }
            }
        }
        // System.out.print(i+" "+j);
        return ans;
    }

    public int dfsHelper(int i, int j , int[][] grid){
        int n = grid.length;
        int m = grid[0].length;
        int sum = 0;
        if(i<0 || j<0 || i>=n || j>=m ||  grid[i][j]==0){
            return 0;
        }
        int currVal = grid[i][j];
        for(int d=0;d<4;d++){
            int ni = i + row[d];
            int nj = j + col[d];
            grid[i][j]=0;
            sum = Math.max(sum,currVal+dfsHelper(ni,nj,grid));
            grid[i][j]=currVal;
        }

        return sum;
    }
}