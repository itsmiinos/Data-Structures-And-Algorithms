// Last updated: 8/13/2025, 8:15:29 PM
class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);// nlogn
        long ans = 0;
        for(int i=0;i<k;i++){
            if(happiness[happiness.length-1-i]-i<=0){
                ans += 0;
            }
            else{
                ans += happiness[happiness.length-1-i]-i;
            }
        }
        return ans;
    }
}