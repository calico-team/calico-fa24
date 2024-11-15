import java.io.*;

class Solution {
    /**
     * Return the height H in which the danger is minimized and satisfies the budget constraints.
     *
     * B: a non-negative integer
     * N: a positive integer
     * S: an array of N integers
     */
    static long solve(long B, int N, long[] S) {
        // YOUR CODE HERE
        return -1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            long B = Long.parseLong(temp[0]);
            int N = Integer.parseInt(temp[1]);
            temp = in.readLine().split(" ");
            long[] S = new long[N];
            for (int j = 0; j < N; j++) {
                S[j] = Long.parseLong(temp[j]);
            }
            out.println(solve(B, N, S));
        }
        out.flush();
    }
}
