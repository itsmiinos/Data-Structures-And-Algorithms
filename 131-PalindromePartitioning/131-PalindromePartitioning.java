// Last updated: 8/13/2025, 8:22:24 PM
class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> a = new ArrayList();
        backtracking(a,new ArrayList(),s,0);
        return a;
    }

    public void backtracking(List<List<String>> a, List<String> path, String s, int start){
        if(start==s.length()){
            a.add(new ArrayList(path));
            return;
        }
        for(int end=start+1;end<=s.length();end++){
            if(isPalindrome(s,start,end-1)){
                path.add(s.substring(start,end));
                backtracking(a,path,s,end);
                path.remove(path.size()-1);
            }
        }
    }

    public boolean isPalindrome(String s, int i , int j){
        while(i<j){
            if(s.charAt(i++)!=s.charAt(j--)){
                return false;
            }
        }
        return true;
    }
}