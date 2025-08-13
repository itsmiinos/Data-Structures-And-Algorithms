// Last updated: 8/13/2025, 8:18:07 PM
class Solution {
    public int shipWithinDays(int[] weights, int days) {
        int lo = calculateLow(weights);
        int hi = calculateHigh(weights);
        int ans = 0;

        while(lo<=hi){
            int mid = lo + (hi - lo) /2;
            int requiredDays = calculateDays(weights,mid);

            if(requiredDays<=days){
                ans = mid;
                hi = mid-1;
            }
            else{
                lo = mid+1;
            }
        }
        return ans;
    }

    public int calculateDays(int [] weights , int mid){
        int days = 1;
        int sum = 0;

        for(int i=0;i<weights.length;i++){
            if(sum + weights[i] > mid){
                days = days+1;
                sum = 0;
            }
            sum = sum + weights[i];
        }
        return days;
    }

    public int calculateLow(int[] weights){
        int ans = Integer.MIN_VALUE;
        for(int i=0;i<weights.length;i++){
            ans = Math.max(ans,weights[i]);
        }
        return ans;
    }

    public int calculateHigh(int[] weights){
        int ans = 0;
        for(int i=0;i<weights.length;i++){
            ans = ans + weights[i];
        }
        return ans;
    }
}