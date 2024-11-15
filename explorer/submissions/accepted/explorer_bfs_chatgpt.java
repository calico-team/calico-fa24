import java.io.*;
import java.util.*;

class Solution {
    static final int N = 500;
    static final int D = 3;
  
    // This function is a translation of the Python solution generated by ChatGPT
    static void solve() throws IOException {
        Set<Integer>[] adjCache = new HashSet[N + 1];
        for (int i = 0; i <= N; i++) {
            adjCache[i] = new HashSet<>();
        }
        
        Queue<Integer> queue = new ArrayDeque<>();
        Map<Integer, Integer> dist = new HashMap<>();
        
        queue.add(1);
        dist.put(1, 0);

        while (!queue.isEmpty()) {
            int currVertex = queue.poll();
            for (int adj : cacheScan(currVertex, adjCache)) {
                if (adj == N) {
                    submit(dist.get(currVertex) + 1);
                    return;
                }
                if (!dist.containsKey(adj)) {
                    dist.put(adj, dist.get(currVertex) + 1);
                    queue.add(adj);
                }
            }
        }
    }
    
    // This one too
    static Set<Integer> cacheScan(int v, Set<Integer>[] adjCache) throws IOException {
        while (adjCache[v].size() < D) {
            int w = scan(v);
            adjCache[v].add(w);
            adjCache[w].add(v);
        }
        return adjCache[v];
    }
    
    static int scan(int v) throws IOException {
        out.println("SCAN " + v);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return Integer.parseInt(response);
    }
    
    static String submit(int d) throws IOException {
        out.println("SUBMIT " + d);
        out.flush();
        String response = in.readLine();
        if (response.equals("WRONG_ANSWER")) {
            System.exit(0);
        }
        return response;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            solve();
        }
    }
}
