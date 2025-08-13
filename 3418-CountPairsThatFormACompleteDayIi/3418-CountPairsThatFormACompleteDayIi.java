// Last updated: 8/13/2025, 8:15:20 PM
class Solution {
    public long countCompleteDayPairs(int[] hours) {
        int n = hours.length;
        long count = 0;
        int freq[] = new int[24];
        for(int i=0;i<n;i++){
            int rem = (24-(hours[i]%24))%24;
            count += freq[rem];
            freq[hours[i]%24]++;
        }

        return count;
    }
}