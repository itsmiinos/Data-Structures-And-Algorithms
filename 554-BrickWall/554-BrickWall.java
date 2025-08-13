// Last updated: 8/13/2025, 8:19:34 PM
class Solution {
    public int leastBricks(List<List<Integer>> wall) {
        int ans = 0;
        HashMap<Integer,Integer> map = new HashMap();
        for(List<Integer> walls : wall){
            int g = 0;
            for(int i=0;i<walls.size()-1;i++){
                g += walls.get(i);
                map.put(g,map.getOrDefault(g,0)+1);
                ans  = Math.max(map.get(g),ans);
            }
        }
        return wall.size()-ans;
    }
}