// Last updated: 8/13/2025, 8:19:03 PM
class Solution {
    public int openLock(String[] deadends, String target) {
        HashSet<String> dead_ends = new HashSet(Arrays.asList(deadends));
        HashSet<String> visited = new HashSet();
        visited.add("0000");

        Queue<String> queue = new LinkedList();
        queue.add("0000");
        int level = 0;
        while(!queue.isEmpty()){
            int size = queue.size();
            while(size>0){
                String rem = queue.remove();
                if(dead_ends.contains(rem)){
                    size--;
                    continue;
                }
                if(rem.equals(target)){
                    return level;
                }
                StringBuilder sb = new StringBuilder(rem);
                for(int i=0;i<4;i++){
                    char current_position = sb.charAt(i);
                    String s1 = sb.substring(0,i)+(current_position=='9'?0:current_position - '0'+1)+sb.substring(i+1);
                    String s2 = sb.substring(0,i)+(current_position=='0'?9:current_position - '0'-1)+sb.substring(i+1);
                    if(!visited.contains(s1)&&!dead_ends.contains(s1)){
                        queue.add(s1);
                        visited.add(s1);
                    }
                    if(!visited.contains(s2)&&!dead_ends.contains(s2)){
                        queue.add(s2);
                        visited.add(s2);
                    }
                }
                size--;
            }
            level++;
        }
        return -1;
    }
}

