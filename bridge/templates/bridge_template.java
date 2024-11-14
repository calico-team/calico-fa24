import java.io.*;

class Solution {
    /**
     * Return the sum of A and B.
     *
     * B: a non-negative integer
     * N: a positive integer
     * S: an array of N integers
     */
    static int solve(int B, int N, int[] S) {
        // YOUR CODE HERE
        return -1;
    }

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) throws IOException {
        int T = Integer.parseInt(in.readLine());
        for (int i = 0; i < T; i++) {
            String[] temp = in.readLine().split(" ");
            int B = Integer.parseInt(temp[0]), N = Integer.parseInt(temp[1]);
            int[] S = new int[N];
            for (int j = 0; j < N; j++) {
                S[j] = Integer.parseInt(in.readLine());
            }
            out.println(solve(B, N, S));
        }
        out.flush();
    }
}
