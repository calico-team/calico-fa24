import java.io.*;

class Solution {
    /**
     * Output the true difficulty of each trail given
     * a mountain range with N checkpoints and M trails
     * between them.
     * 
     * N: the number of vertices in the graph
     * M: the number of edges
     * F: France
     * S: Spain
     * E: the list edges in [u, v, w] format
     */
    static void solve(int N, int M, int F, int S, int[][] E) {
        // YOUR CODE HERE
        return;
    }
    
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] info = in.readLine().split(" ");
            int N = Integer.parseInt(info[0]);
            int M = Integer.parseInt(info[1]);
            int F = Integer.parseInt(info[2]);
            int S = Integer.parseInt(info[3]);
            int[][] E = new int[][M];
            for (int j = 0; j < M; j++) {
                String[] trail = in.readLine().split(" ");
                e = new int[3];
                e[0] = Integer.parseInt(trail[0]);
                e[1] = Integer.parseInt(trail[1]);
                e[2] = Integer.parseInt(trail[2]);
                E[i] = e;
            }
            solve(N, M, F, S, E);
        }
        out.flush();
    }
}