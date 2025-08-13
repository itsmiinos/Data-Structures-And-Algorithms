// Last updated: 8/13/2025, 8:20:07 PM
class Solution {
    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        ArrayList<Integer> ans = new ArrayList();
        if(n==1 || n==2){
            for(int i =0;i<n;i++){
                ans.add(i);
            }
        }
        int[] degree = new int[n];
        ArrayList<ArrayList<Integer>>adj = new ArrayList();
        for(int i=0;i<n;i++){
            adj.add(new ArrayList());
        }
        for(int[] edge : edges){
            int u = edge[0];
            int v = edge[1];
            adj.get(u).add(v);
            adj.get(v).add(u);
            degree[u]++;
            degree[v]++;
        }
        Queue<Integer> q = new LinkedList();
        for(int i=0;i<n;i++){
            if(degree[i]==1){
                q.add(i);
                degree[i]--;
            }
        }
        while(!q.isEmpty()){
            ans = new ArrayList();
            int size = q.size();
            for(int i=0;i<size;i++){
                int rem = q.remove();
                ans.add(rem);
                for(int nbr : adj.get(rem)){
                    degree[nbr]--;
                    if(degree[nbr]==1)q.add(nbr);
                }
            }
        }
        return ans;

    }
}