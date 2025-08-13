// Last updated: 8/13/2025, 8:22:00 PM
class Solution {
    public String reverseWords(String s) {
        String splitted[] = s.trim().split("\\s+");
        String ans = "";
        for(int i = splitted.length-1; i>=1;i--){
            if(splitted[i]!="" || splitted[i]!=" "){
           
                ans = ans+splitted[i]+" ";
            }
        }
        if(splitted[0]!=" "){
            ans = ans+splitted[0];
        }
        System.out.print(splitted.length);
        return ans;
        
    }
}