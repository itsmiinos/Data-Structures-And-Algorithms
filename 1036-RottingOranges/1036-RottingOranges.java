// Last updated: 8/13/2025, 8:18:10 PM
class Solution {
    class Pair{
        int n;
        int m;
        int t;
        Pair(int n,int m,int t){
            this.n = n;
            this.m = m;
            this.t = t;
        }
    }
    public int orangesRotting(int[][] grid) {
        int count1=0;
        int count2=0;
        int n = grid.length;
        int m = grid[0].length;
        Queue<Pair> q = new LinkedList();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==2){
                    count2++;
                    q.add(new Pair(i,j,0));
                }
                if(grid[i][j]==1){
                    count1++;
                }
            }
        }
        if(count1==0){
            return 0;
        }
        if(count2==0){
            return -1;
        }
        int ans=-1;
        while(q.size()>0){
            Pair r = q.remove();
            int i = r.n;
            int j = r.m;
            int t = r.t;
            ans = r.t;
            if(i+1<n && grid[i+1][j]==1){
                q.add(new Pair(i+1,j,t+1));
                grid[i+1][j] = 2;
            }
            if(i-1>=0 && grid[i-1][j]==1){
                q.add(new Pair(i-1,j,t+1));
                grid[i-1][j]=2;
            }
            if(j+1<m && grid[i][j+1]==1){
                q.add(new Pair(i,j+1,t+1));
                grid[i][j+1]=2;
            }
            if(j-1>=0 && grid[i][j-1]==1){
                q.add(new Pair(i,j-1,t+1));
                grid[i][j-1]=2;
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==1){
                    return -1;
                }
            }
        }
        return ans;
    }
}