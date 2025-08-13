// Last updated: 8/13/2025, 8:17:07 PM
class Solution {
    public int maxDepth(String s) {
        int maxDepth = 0;
        int depth = 0;
        Stack<Character> st = new Stack();
        for(int i=0;i<s.length();i++){
            if(s.charAt(i)=='(' || s.charAt(i)==')'){
                if(st.size()==0){
                    st.push(s.charAt(i));
                }
                if(s.charAt(i)==')' && st.peek()=='('){
                    st.pop();
                    depth--;
                }
                if(s.charAt(i)=='(' && st.peek()=='('){
                    depth++;
                    st.push(s.charAt(i));
                }
            }
            maxDepth = Math.max(maxDepth , depth);
        }
        return maxDepth;
    }
}