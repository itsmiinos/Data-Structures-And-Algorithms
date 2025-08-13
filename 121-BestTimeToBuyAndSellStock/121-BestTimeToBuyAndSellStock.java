// Last updated: 8/13/2025, 8:22:38 PM
class Solution {
    public int maxProfit(int[] prices) {
        int prefixMin[] = new int[prices.length];
        int suffixMax[] = new int[prices.length];

        prefixMin[0] = prices[0];
        for(int i=1;i<prices.length;i++){
            prefixMin[i] = Math.min(prefixMin[i-1],prices[i]);
        }

        suffixMax[prices.length-1] = prices[prices.length-1];
        for(int i=prices.length-2; i >=0;i--){
            suffixMax[i] = Math.max(suffixMax[i+1],prices[i]);
        }
        int profit = 0;
        int maxProfit = 0;
        for(int i=0;i<prices.length;i++){
            if((suffixMax[i] - prefixMin[i])>0){
                profit = suffixMax[i] - prefixMin[i];
            }
            maxProfit = Math.max(profit , maxProfit);
        }
        return maxProfit;
    }
}