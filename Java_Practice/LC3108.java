import java.util.Arrays;

public class LC3108 {
    public static void main(String[] args) {
        int n = 5;
        int[][] edges = { { 0, 1, 7 }, { 1, 3, 7 }, { 1, 2, 1 } };
        int[][] query = { { 0, 3 }, { 3, 4 } };

        int[] parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
        int[] min_cost_path = new int[n];
        Arrays.fill(min_cost_path, -1);
        int[] results = new int[query.length];

        for (int i = 0; i < edges.length; i++) {
            int source_root = find(parent, edges[i][0]);
            int target_root = find(parent, edges[i][1]);

            min_cost_path[target_root] &= edges[i][2];

            if (source_root != target_root) {
                min_cost_path[target_root] &= min_cost_path[source_root];
                parent[source_root] = target_root;
            }
        }

        for (int i = 0; i < query.length; i++) {
            if (query[i][0] == query[i][1]) {
                results[i] = 0;
            } else if (find(parent, query[i][0]) != find(parent, query[i][1])) {
                results[i] = -1;
            } else {
                results[i] = min_cost_path[find(parent, query[i][0])];
            }
        }
        System.out.println(Arrays.toString(results));
        System.out.println(Arrays.toString(parent));
        System.out.println(Arrays.toString(min_cost_path));
    }

    public static int find(int[] parent, int node) {
        if (node == parent[node]) {
            return node;
        } else {
            return find(parent, parent[node]);
        }
    }
}