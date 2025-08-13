// Last updated: 8/13/2025, 8:18:24 PM
class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        int n = deck.length;
        HashMap<Integer,Integer> h = new HashMap();
        for(int i=0;i<n;i++){
            if(h.containsKey(deck[i])==false){
                h.put(deck[i],1);
            }
            else{
                int temp = h.get(deck[i]);
                h.put(deck[i],temp+1);
            }
        }
        int ans = 0;
        for(int key : h.keySet()){
            ans = gcd(h.get(key),ans);
        }
        if(ans==1){
            return false;
        }
        return true;
    }

    public int gcd(int a , int b){
        if(a==0){
            return b;
        }
        int temp = gcd(b%a,a);
        return temp;
    }
}