// Last updated: 8/13/2025, 8:15:36 PM
class Solution {
    public long minimumSteps(String s) {
        char[] c = s.toCharArray();
        int countOfBlackBalls = 0;
        long count=0;
        for(int i=0;i<c.length;i++){
            if(c[i]=='0'){
                count += countOfBlackBalls;
            }
            else{
                countOfBlackBalls++;
            }
        }
        // return count;









        // int firstOneIndex = -1;
        // for(int i=0;i<c.length;i++){
        //     if(c[i]=='1'){
        //         firstOneIndex = i;
        //         break;
        //     }
        // }
        // if(firstOneIndex == -1){
        //     return 0;
        // }
        // long count = 0;
        // int j = firstOneIndex;
        // int i = firstOneIndex;
        // while(j<c.length){
        //     if(c[j]=='0'){
        //         char temp = c[i];
        //         c[i] = c[j];
        //         c[j] = temp;
        //         i = j;
        //         count++;
        //     }
        //     j++;
        // }
        return count;
    }
}