// Last updated: 8/13/2025, 8:15:41 PM
class Solution {
    public int minLength(String s) {
        char[] ch = s.toCharArray();
        int i=0;
        int j=1;
        while(j<ch.length){
            if(i==-1){
                i++;
                ch[i] = ch[j];
            }
            else if(ch[j]=='B' && ch[i]=='A'){
                i--;
            }
            else if(ch[j]=='D' && ch[i]=='C'){
                i--;
            }
            else{
                i++;
                ch[i] = ch[j];
            }
            j++;
        }

        return i+1;














        // Stack<Character> st = new Stack();
        // char[] ch = s.toCharArray();
        // for(char c : ch){
        //     if(st.size()==0){
        //         st.push(c);
        //         continue;
        //     }
        //     if(c=='B' && st.peek()=='A'){
        //         st.pop();
        //     }
        //     else if(c=='D' && st.peek()=='C'){
        //         st.pop();
        //     }
        //     else{
        //         st.push(c);
        //     }
        // }

        // return st.size();
    }
}