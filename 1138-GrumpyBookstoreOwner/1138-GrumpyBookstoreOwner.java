// Last updated: 8/13/2025, 8:17:48 PM
class Solution {
    public int maxSatisfied(int[] customer, int[] grumpy, int minutes) {
        int n = customer.length;
        int windowSum = 0;
        int zeroSum = 0;
        int maxSum = Integer.MIN_VALUE;
        
        for(int i=0;i<n;i++){
            if(grumpy[i]==0){
                zeroSum += customer[i];
            }
            if(i<minutes){
                if(grumpy[i]==1){
                    windowSum += customer[i];
                }
            }
            else{
                windowSum += (grumpy[i]==1 ? customer[i] : 0) - (grumpy[i-minutes]==1 ? customer[i-minutes] : 0);
            }
            maxSum = Math.max(maxSum , windowSum);
        }

        return maxSum + zeroSum;
    }
}