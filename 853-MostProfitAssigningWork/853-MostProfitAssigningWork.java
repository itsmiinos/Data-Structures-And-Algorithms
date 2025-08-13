// Last updated: 8/13/2025, 8:18:45 PM
class Solution {
    public int maxProfitAssignment(int[] difficulty, int[] profit, int[] worker) {
        int n = difficulty.length;
        int m = worker.length;
        int[][] job = new int[n][2];
        for(int i=0;i<n;i++){
            job[i][0] = difficulty[i];
            job[i][1] = profit[i];
        }

        Arrays.sort(job, (a,b) -> a[0] - b[0]);
        Arrays.sort(worker);
        int maxProfit = 0;
        int i = 0;
        int best = 0;
        for(int ability : worker){
            while(i<n && ability>=job[i][0]){
                best = Math.max(best, job[i][1]);
                i++;
            }
            maxProfit += best;
        }

        return maxProfit;
    }
}