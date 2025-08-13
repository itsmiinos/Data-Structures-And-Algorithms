// Last updated: 8/13/2025, 8:15:19 PM
class Solution {
    public int countCompleteDayPairs(int[] hours) {
        int n = hours.length;
        int count = 0;
        int freq[] = new int[24];
        for(int i=0;i<n;i++){
            int rem = (24 - (hours[i]%24))%24;
            count += freq[rem];
            freq[(hours[i]%24)]++;
            //System.out.print(rem+" ");
        }
        return count;
    }
}