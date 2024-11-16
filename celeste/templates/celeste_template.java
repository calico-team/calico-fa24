import java.io.*;

class Solution {
    /**
     * Return the minimum number of moves to get to E, or return 
     * -1 if it is impossible.
     * 
     * N: number of rows
     * M: number of columns
     * K: the length of Madeline’s dash
     * C: a list of N strings with M characters each, describing 
     * the maze Madeline is in.
     *    In each string:
     *     . denotes a space
     *     # denotes a wall.
     *     * denotes a dash crystal.
     *     S denotes Madeline’s start tile.
     *     E denotes Madeline’s end tile.
     */
    static int solve(int N, int M, int K, String[] C) {
        // YOUR CODE HERE
        return -1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int tc = 0; tc < T; tc++) {
            String[] temp = in.readLine().split(" ");
            int N = Integer.parseInt(temp[0]);
            int M = Integer.parseInt(temp[1]);
            int K = Integer.parseInt(temp[2]);
            String[] C = new String[N];
            for (int i = 0; i < N; ++i) {
                C[i] = in.readLine();
            }
            out.println(solve(N, M, K, C));
        }
        out.flush();
    }
}
