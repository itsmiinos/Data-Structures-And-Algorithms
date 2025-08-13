// Last updated: 8/13/2025, 8:20:44 PM
import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        int slength = s.length();
        int tlength = t.length();
        if(slength!=tlength){
            return false;
        }
        char[] s1 = s.toCharArray();
        char[] t1 = t.toCharArray();
        Arrays.sort(s1);
        Arrays.sort(t1);
        for(int i=0;i<s.length();i++){
            if(s1[i]!=t1[i]){
                return false;
            }
        }
        return true;
    }
}