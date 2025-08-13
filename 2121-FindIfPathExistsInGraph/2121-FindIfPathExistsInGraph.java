// Last updated: 8/13/2025, 8:16:39 PM
class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        ArrayList<ArrayList<Integer>> graph = new ArrayList();
        for(int i=0;i<n;i++){
            graph.add(new ArrayList());
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        boolean[] visited = new boolean[n];
        // visited[source] = true;
        validPathHelper(graph,visited,source);
        return visited[destination];
    }

    public void validPathHelper(ArrayList<ArrayList<Integer>> graph, boolean[] visited, int src){
        if (visited[src]) return;
        visited[src] = true;
        for (int child : graph.get(src)) {
            if (!visited[child])
                validPathHelper(graph,visited,child);
        }
    }
}