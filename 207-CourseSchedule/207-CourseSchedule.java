// Last updated: 8/13/2025, 8:21:22 PM
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList();
        for(int i=0;i<numCourses;i++){
            adj.add(new ArrayList());
        }
        for(int[] i : prerequisites){
            int u = i[0];
            int v = i[1];

            adj.get(u).add(v);
        }
        int[] indegree = new int[numCourses];
        for(int i=0;i<numCourses;i++){
            for(int v : adj.get(i)){
                indegree[v]++;
            }
        }
        Queue<Integer> q = new LinkedList();
        for(int i=0;i<numCourses;i++){
            if(indegree[i]==0){
                q.add(i);
            }
        }
        if(q.size()==0)return false;
        while(!q.isEmpty()){
            int rem = q.remove();
            for(int v:adj.get(rem)){
                indegree[v]--;
                if(indegree[v]==0)q.add(v);
            }
        }
        for(int i=0;i<numCourses;i++){
            if(indegree[i]>0){
                return false;
            }
        }
        return true;
    }
}