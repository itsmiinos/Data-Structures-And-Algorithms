// Last updated: 8/13/2025, 8:16:32 PM
class Solution {
    public int minSwaps(String s) {
        int size = 0;
        int i=0;
        while(i<s.length()){
            if(s.charAt(i)=='['){
                size++;
            }
            else if(size>0){
                size--;
            }
            i++;
        }
        return (size+1)/2;
    }
}