import java.util.*;

public class LC1976 {

    public int countPaths(int n, int[][] roads) {
        List<List<int[]>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] road : roads) {
            int x = road[0], y = road[1], time = road[2];

            graph.get(x).add(new int[] { y, time });
            graph.get(y).add(new int[] { x, time });
        }

        int[] ways = new int[n];
        ways[0] = 1;

        long[] dist = new long[n];
        Arrays.fill(dist, Long.MAX_VALUE);
        dist[0] = 0;

        PriorityQueue<long[]> pq = new PriorityQueue<>(Comparator.comparingLong(a -> a[0]));
        pq.offer(new long[] { 0, 0 });

        while (!pq.isEmpty()) {
            long[] curr = pq.poll();
            long target = curr[0];
            int node = (int) curr[1];

            if (target > dist[node])
                continue;
            for (int[] neighbour : graph.get(node)) {
                int nextNode = neighbour[0];
            }
        }
        return 0;
    }

    public static void main(String[] args) {
    }
}