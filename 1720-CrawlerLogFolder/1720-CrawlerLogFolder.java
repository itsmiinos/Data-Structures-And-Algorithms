// Last updated: 8/13/2025, 8:17:09 PM
class Solution {
    public int minOperations(String[] logs) {
        int ans = 0;
        for(String i : logs){
            if(i.equals("../")){
                if(ans>0){
                    ans--;
                }
            }
            else if(!i.equals("./")){
                ans++;
            }
        }

        return ans;
    }
}