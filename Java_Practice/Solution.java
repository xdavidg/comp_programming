import java.util.*;

public class Solution {
    private int[] parent;
    private int[] rank;

    public Solution(int size) {
        this.parent = new int[size];
        for (int i = 0; i < size; i++) {
            parent[i] = i;
        }
        this.rank = new int[size];
    }

    public int find(int[] parent, int node) {
        if (node != parent[node]) {
            node = find(parent, parent[node]);
        }
        return node;
    }

    public void union(int[] parent, int[] edge) {
        int source_root = find(parent, edge[0]);
        int target_root = find(parent, edge[1]);

        if (source_root == target_root) {
            return;
        }

        if (rank[source_root] < rank[target_root]) {
            parent[target_root] = source_root;
        } else if (rank[source_root] > rank[target_root]) {
            parent[source_root] = target_root;
        } else {
            parent[target_root] = source_root;
            rank[source_root]++;
        }
    }

    public int countCompleteComponents(int n, int[][] edges) {
        Solution uf = new Solution(n);

        for (int[] edge : edges) {
            uf.union(uf.parent, edge);
        }

        HashMap<Integer, Set<Integer>> compVertices = new HashMap<>();
        HashMap<Integer, Integer> compEdges = new HashMap<>();

        for (int i = 0; i < n; i++) {
            int root = uf.find(uf.parent, i);
            if (!compVertices.containsKey(root)) {
                compVertices.put(root, new HashSet<>());
            }
            compVertices.get(root).add(i);
        }

        for (int[] edge : edges) {
            int root = uf.find(uf.parent, edge[0]);
            compEdges.put(root, compEdges.getOrDefault(root, 0) + 1);
        }

        int completeCount = 0;
        for (int root : compVertices.keySet()) {
            int numVertices = compVertices.get(root).size();
            int expectedEdges = numVertices * (numVertices - 1) / 2;

            if (compEdges.getOrDefault(root, 0) == expectedEdges) {
                completeCount++;
            }
        }

        return completeCount;
    }
}