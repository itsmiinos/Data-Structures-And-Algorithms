// Last updated: 8/13/2025, 8:15:30 PM
class Solution {
    public boolean isValid(String word) {
        if(word.length()<3){
            return false;
        }
        int vow = 0;
        int con = 0;
        word = word.toLowerCase();
        char[] c = word.toCharArray();
        for(int i=0;i<c.length;i++){
            if (!Character.isLetter(c[i]) && !Character.isDigit(c[i])) {
                return false;
            }
            if(c[i]=='a'||c[i]=='e'||c[i]=='i'||c[i]=='o'||c[i]=='u'){
                vow++;
            }
            if(c[i]!='a' && c[i]!='e' && c[i]!='i' && c[i]!='o' && c[i]!='u' && (int)c[i]>=97 && (int)c[i]<=122){
                con++;
            }
        }
        if(vow>0 && con>0){
            return true;
        }
        return false;
    }
}