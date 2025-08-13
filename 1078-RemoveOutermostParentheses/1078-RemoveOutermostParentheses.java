// Last updated: 8/13/2025, 8:17:59 PM
class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> st = new Stack();
        String ans = "";
        for(int i=0;i<s.length();i++){
            if(st.size()==0){
                st.push(s.charAt(i));
            }
            else if(st.size()==1 && st.peek()=='(' && s.charAt(i)==')'){
                st.pop();
            }
            else if(st.size()>=1 && s.charAt(i)=='('){
                ans = ans+s.charAt(i);
                st.push(s.charAt(i));
            }
            else if(st.size()>=1 && st.peek()=='(' && s.charAt(i)==')'){
                st.pop();
                ans = ans + s.charAt(i);
            }
        }
        System.out.print(ans);
        return ans;
    }
}