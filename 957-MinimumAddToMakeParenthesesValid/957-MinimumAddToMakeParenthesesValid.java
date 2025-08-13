// Last updated: 8/13/2025, 8:18:14 PM
class Solution {
    public int minAddToMakeValid(String s) {
        int size = 0;
        int open = 0;
        Stack<Character> st = new Stack();
        for(int i=0;i<s.length();i++){
            // if(st.size()==0){
            //     st.push(s.charAt(i));
            // }
            // else if(s.charAt(i)==')' && st.peek()=='('){
            //     st.pop();
            // }
            // else{
            //     st.push(s.charAt(i));
            // }
            if(s.charAt(i)=='('){
                size++;
            }
            else if(size>0){
                size--;
            }
            else{
                open++;
            }
        }
        return (size+open);
    }
}